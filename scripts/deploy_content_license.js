// scripts/deploy_content_license.js
async function main() {
  const [deployer] = await ethers.getSigners();
  console.log(`Deploying contract with address: ${deployer.address}`);

  const ContentLicense = await ethers.getContractFactory("ContentLicense");
  const contentLicense = await ContentLicense.deploy(10); // Deploy with a 10% royalty percentage

  await contentLicense.deployed();

  console.log(`Contract deployed to address: ${contentLicense.address}`);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
