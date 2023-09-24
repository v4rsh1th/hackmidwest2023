const ContentLicense = artifacts.require("ContentLicense");

module.exports = function (deployer) {
    deployer.deploy(ContentLicense, 10, { gas: 5000000 }); // 10% royalty percentage
};