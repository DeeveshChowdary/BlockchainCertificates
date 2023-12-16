// contracts/TransactionContract.sol

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract TransactionContract {
    event TransactionMade(address indexed from, address indexed to, string jsonData);

    function sendTransaction(address to, string memory jsonData) public {
        emit TransactionMade(msg.sender, to, jsonData);
    }
}

