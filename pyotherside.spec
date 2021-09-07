#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyotherside
Version  : 1.5.9
Release  : 17
URL      : https://github.com/thp/pyotherside/archive/1.5.9/pyotherside-1.5.9.tar.gz
Source0  : https://github.com/thp/pyotherside/archive/1.5.9/pyotherside-1.5.9.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : ISC
Requires: pyotherside-lib = %{version}-%{release}
Requires: pyotherside-license = %{version}-%{release}
BuildRequires : buildreq-qmake
BuildRequires : mesa-dev
BuildRequires : pkgconfig(Qt5Qml)
BuildRequires : pkgconfig(Qt5Quick)
BuildRequires : pkgconfig(Qt5Svg)
BuildRequires : pkgconfig(Qt5Test)
BuildRequires : python3-dev

%description
PyOtherSide: Asynchronous Python 3 Bindings for Qt 5
====================================================

%package lib
Summary: lib components for the pyotherside package.
Group: Libraries
Requires: pyotherside-license = %{version}-%{release}

%description lib
lib components for the pyotherside package.


%package license
Summary: license components for the pyotherside package.
Group: Default

%description license
license components for the pyotherside package.


%prep
%setup -q -n pyotherside-1.5.9
cd %{_builddir}/pyotherside-1.5.9

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
%qmake -config ltcg -config fat-static-lto
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1581608462
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pyotherside
cp %{_builddir}/pyotherside-1.5.9/LICENSE %{buildroot}/usr/share/package-licenses/pyotherside/4937dca073faf77fa122ef36516efa65e3827428
%make_install

%files
%defattr(-,root,root,-)
/usr/tests/qtquicktests/qtquicktests

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/qml/io/thp/pyotherside/libpyothersideplugin.so
/usr/lib64/qt5/qml/io/thp/pyotherside/pyotherside.qmltypes
/usr/lib64/qt5/qml/io/thp/pyotherside/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pyotherside/4937dca073faf77fa122ef36516efa65e3827428
