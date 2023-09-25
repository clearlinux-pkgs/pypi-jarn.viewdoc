#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-jarn.viewdoc
Version  : 2.7
Release  : 42
URL      : https://files.pythonhosted.org/packages/85/ab/9b5197ca1380c2084647c44655cc225d4783e42aa28108186b9c1cb1fe55/jarn.viewdoc-2.7.tar.gz
Source0  : https://files.pythonhosted.org/packages/85/ab/9b5197ca1380c2084647c44655cc225d4783e42aa28108186b9c1cb1fe55/jarn.viewdoc-2.7.tar.gz
Summary  : Python documentation viewer
Group    : Development/Tools
License  : BSD-2-Clause
Requires: pypi-jarn.viewdoc-bin = %{version}-%{release}
Requires: pypi-jarn.viewdoc-python = %{version}-%{release}
Requires: pypi-jarn.viewdoc-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
============
jarn.viewdoc
============
------------------------------------
Python documentation viewer
------------------------------------

%package bin
Summary: bin components for the pypi-jarn.viewdoc package.
Group: Binaries

%description bin
bin components for the pypi-jarn.viewdoc package.


%package python
Summary: python components for the pypi-jarn.viewdoc package.
Group: Default
Requires: pypi-jarn.viewdoc-python3 = %{version}-%{release}

%description python
python components for the pypi-jarn.viewdoc package.


%package python3
Summary: python3 components for the pypi-jarn.viewdoc package.
Group: Default
Requires: python3-core
Provides: pypi(jarn.viewdoc)
Requires: pypi(blessed)
Requires: pypi(docutils)
Requires: pypi(pygments)
Requires: pypi(setuptools)

%description python3
python3 components for the pypi-jarn.viewdoc package.


%prep
%setup -q -n jarn.viewdoc-2.7
cd %{_builddir}/jarn.viewdoc-2.7
pushd ..
cp -a jarn.viewdoc-2.7 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1695654198
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/viewdoc

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
