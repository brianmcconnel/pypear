echo "Remove old builds..."
rm -rf build
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
git-archive-all build/pypear.tar.gz
echo "Unzip build"
tar -xf build/pypear.tar.gz
