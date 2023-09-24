const ContentLicense = artifacts.require("ContentLicense");

module.exports = function (deployer) {
    deployer.deploy(ContentLicense, 10); // 10% royalty percentage
};
