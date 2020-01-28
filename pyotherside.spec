#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyotherside
Version  : 1.5.8
Release  : 10
URL      : https://github.com/thp/pyotherside/archive/1.5.8/pyotherside-1.5.8.tar.gz
Source0  : https://github.com/thp/pyotherside/archive/1.5.8/pyotherside-1.5.8.tar.gz
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
%setup -q -n pyotherside-1.5.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
%qmake -config ltcg
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1560705515
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pyotherside
cp LICENSE %{buildroot}/usr/share/package-licenses/pyotherside/LICENSE
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
/usr/share/package-licenses/pyotherside/LICENSE
