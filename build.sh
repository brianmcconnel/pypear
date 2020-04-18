BUILD=$(date +"%Y.%m.%d%H%M")
echo "Building pypear..."
echo "pypear-$BUILD"
echo "Submodule init..."
git submodule update --init
echo "Installing git-archive-all..."
pip install git-archive-all
echo "Making build..."
mkdir -p build
echo "Creating build archive..."
git-archive-all build/pypear-$BUILD.tar.gz
echo "Generating hash for conda-forge..."
openssl sha256 build/pypear-$BUILD.tar.gz
