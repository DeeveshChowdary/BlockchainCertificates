pragma solidity ^0.6.0;

contract Register{
    uint256 public studentId;
    uint256 public registerId;
    uint256 public collegeId;
    uint256 public courseId;

    /** constructor(
        string memory _name,
        string memory _symbol,
        uint256 _decimals,
        uint256 _totalSupply
    )
        public
    {
        name = _name;
        symbol = _symbol;
        decimals = _decimals;
        totalSupply = _totalSupply;
        balances[msg.sender] = _totalSupply;
        emit Transfer(address(0), msg.sender, _totalSupply);
    }*/



    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    function transfer(address _to, uint256 _value) public returns (bool) {
        metadata[_to] = _metadata
        emit Transfer(msg.sender, to, value);
        return true;
    }

    function approve(address spender, uint256 value) public returns (bool) {
    require(spender != address(0));
    emit Approval(msg.sender, spender, value);
    return true;
  }
 






}