// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ContentLicense {
    address public owner;
    uint256 public royaltyPercentage;
    mapping(address => uint256) public contentOwners;

    event ContentLicensed(address indexed contentOwner, uint256 amount);

    constructor(uint256 _royaltyPercentage) {
        owner = msg.sender;
        royaltyPercentage = _royaltyPercentage;
    }

    function licenseContent() public payable {
        require(msg.value > 0, "Payment required");
        uint256 royaltyAmount = (msg.value * royaltyPercentage) / 100;
        contentOwners[msg.sender] += royaltyAmount;
        emit ContentLicensed(msg.sender, msg.value);
    }

    function withdrawRoyalties() public {
        uint256 royalty = contentOwners[msg.sender];
        contentOwners[msg.sender] = 0;
        payable(msg.sender).transfer(royalty);
    }
}
