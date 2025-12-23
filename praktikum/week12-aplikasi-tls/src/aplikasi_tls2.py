import ssl
import socket
from datetime import datetime

def tls_connection(hostname, port=443):
    print("=" * 60)
    print("SIMULASI KONEKSI TLS (Transport Layer Security)")
    print("=" * 60)

    # Membuat context TLS standar
    context = ssl.create_default_context()

    # Membuat socket TCP
    with socket.create_connection((hostname, port)) as sock:
        # Membungkus socket dengan TLS
        with context.wrap_socket(sock, server_hostname=hostname) as tls_socket:
            print(f"[INFO] Berhasil terhubung ke {hostname}:{port}")
            print(f"[INFO] Versi TLS      : {tls_socket.version()}")
            print(f"[INFO] Cipher Suite   : {tls_socket.cipher()[0]}")
            print("-" * 60)

            # Mengambil sertifikat server
            cert = tls_socket.getpeercert()

            print("INFORMASI SERTIFIKAT DIGITAL")
            print("-" * 60)

            subject = dict(x[0] for x in cert['subject'])
            issuer = dict(x[0] for x in cert['issuer'])

            print(f"Nama Domain (CN) : {subject.get('commonName')}")
            print(f"Issuer (CA)      : {issuer.get('commonName')}")

            not_before = cert['notBefore']
            not_after = cert['notAfter']

            print(f"Berlaku Mulai    : {not_before}")
            print(f"Berlaku Hingga   : {not_after}")

            print("-" * 60)

            # Cek masa berlaku sertifikat
            expire_date = datetime.strptime(not_after, "%b %d %H:%M:%S %Y %Z")
            if expire_date > datetime.utcnow():
                print("[STATUS] Sertifikat MASIH VALID")
            else:
                print("[STATUS] Sertifikat SUDAH KADALUARSA")

            print("=" * 60)
            print("KONEKSI TLS AMAN BERHASIL DILAKUKAN")
            print("=" * 60)


if __name__ == "__main__":
    # Ganti domain sesuai kebutuhan praktikum
    target_domain = "www.tokopedia.com"
    tls_connection(target_domain)
