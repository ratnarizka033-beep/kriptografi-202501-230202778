SPDX-License-Identifier: MIT
pragma 

TinyCoin - Smart Contract ERC20 Sederhana
Nama  : TinyCoin
Simbol      : TNC
Total: 1.000.000 TNC

contract TinyCoin {

    string public name = "TinyCoin";
    string public symbol = "TNC";
    uint8 public decimals = 18;
    uint256 public totalSupply;

Menyimpan saldo setiap alamat
(address =uint256) public balanceOf;

    // Menyimpan izin transfer (allowance)
    mapping(address => mapping(address => uint256)) public allowance;

    // Event standar ERC20
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Constructor: dijalankan saat kontrak dideploy
    constructor(uint256 _initialSupply) {
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balanceOf[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    // Fungsi transfer token
    function transfer(address _to, uint256 _value) public returns (bool success) {
        require(balanceOf[msg.sender] >= _value, "Saldo tidak mencukupi");
        require(_to != address(0), "Alamat tujuan tidak valid");

        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;

        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    // Fungsi approve (izin transfer)
    function approve(address _spender, uint256 _value) public returns (bool success) {
        allowance[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    // Fungsi transferFrom (transfer dengan izin)
    function transferFrom(
        address _from,
        address _to,
        uint256 _value
    ) public returns (bool success) {

        require(balanceOf[_from] >= _value, "Saldo tidak mencukupi");
        require(allowance[_from][msg.sender] >= _value, "Allowance tidak cukup");
        require(_to != address(0), "Alamat tujuan tidak valid");

        balanceOf[_from] -= _value;
        balanceOf[_to] += _value;
        allowance[_from][msg.sender] -= _value;

        emit Transfer(_from, _to, _value);
        return true;
    }
}



