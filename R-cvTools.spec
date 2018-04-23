#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-cvTools
Version  : 0.3.2
Release  : 5
URL      : https://cran.r-project.org/src/contrib/cvTools_0.3.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/cvTools_0.3.2.tar.gz
Summary  : Cross-validation tools for regression models
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-robustbase
BuildRequires : R-robustbase
BuildRequires : clr-R-helpers

%description
cross-validation with minimal programming effort and assist
        users with model selection.

%prep
%setup -q -c -n cvTools

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523297107

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1523297107
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library cvTools
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library cvTools
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library cvTools
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library cvTools|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/cvTools/DESCRIPTION
/usr/lib64/R/library/cvTools/INDEX
/usr/lib64/R/library/cvTools/Meta/Rd.rds
/usr/lib64/R/library/cvTools/Meta/features.rds
/usr/lib64/R/library/cvTools/Meta/hsearch.rds
/usr/lib64/R/library/cvTools/Meta/links.rds
/usr/lib64/R/library/cvTools/Meta/nsInfo.rds
/usr/lib64/R/library/cvTools/Meta/package.rds
/usr/lib64/R/library/cvTools/NAMESPACE
/usr/lib64/R/library/cvTools/NEWS
/usr/lib64/R/library/cvTools/R/cvTools
/usr/lib64/R/library/cvTools/R/cvTools.rdb
/usr/lib64/R/library/cvTools/R/cvTools.rdx
/usr/lib64/R/library/cvTools/doc/examples/example-accessors.R
/usr/lib64/R/library/cvTools/doc/examples/example-aggregate.R
/usr/lib64/R/library/cvTools/doc/examples/example-bwplot.R
/usr/lib64/R/library/cvTools/doc/examples/example-cvFit.R
/usr/lib64/R/library/cvTools/doc/examples/example-cvReshape.R
/usr/lib64/R/library/cvTools/doc/examples/example-cvSelect.R
/usr/lib64/R/library/cvTools/doc/examples/example-cvTool.R
/usr/lib64/R/library/cvTools/doc/examples/example-cvTuning.R
/usr/lib64/R/library/cvTools/doc/examples/example-densityplot.R
/usr/lib64/R/library/cvTools/doc/examples/example-dotplot.R
/usr/lib64/R/library/cvTools/doc/examples/example-plot.R
/usr/lib64/R/library/cvTools/doc/examples/example-repCV.R
/usr/lib64/R/library/cvTools/doc/examples/example-subset.R
/usr/lib64/R/library/cvTools/doc/examples/example-summary.R
/usr/lib64/R/library/cvTools/doc/examples/example-xyplot.R
/usr/lib64/R/library/cvTools/help/AnIndex
/usr/lib64/R/library/cvTools/help/aliases.rds
/usr/lib64/R/library/cvTools/help/cvTools.rdb
/usr/lib64/R/library/cvTools/help/cvTools.rdx
/usr/lib64/R/library/cvTools/help/paths.rds
/usr/lib64/R/library/cvTools/html/00Index.html
/usr/lib64/R/library/cvTools/html/R.css
/usr/lib64/R/library/cvTools/tests/test-cvFit-once.R
/usr/lib64/R/library/cvTools/tests/test-cvFit-repeated.R
/usr/lib64/R/library/cvTools/tests/test-cvTool-once.R
/usr/lib64/R/library/cvTools/tests/test-cvTool-repeated.R
/usr/lib64/R/library/cvTools/tests/test-cvTuning-once.R
/usr/lib64/R/library/cvTools/tests/test-cvTuning-repeated.R
