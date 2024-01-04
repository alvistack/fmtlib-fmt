# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: fmtlib
Epoch: 100
Version: 11.1.3
Release: 1%{%dist}
Summary: Small, safe and fast formatting library for C++
License: MIT
URL: https://github.com/fmtlib/fmt/tags
Source0: %{name}_%{version}.orig.tar.gz
%if 0%{?rhel} == 7
BuildRequires: devtoolset-11
BuildRequires: devtoolset-11-gcc
BuildRequires: devtoolset-11-gcc-c++
BuildRequires: devtoolset-11-libatomic-devel
%endif
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: ninja-build
BuildRequires: pkgconfig

%description
C++ Format is an open-source formatting library for C++. It can be used
as a safe alternative to printf or as a fast alternative to IOStreams.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%if 0%{?rhel} == 7
. /opt/rh/devtoolset-11/enable
%endif
%cmake \
    -DFMT_DOC=OFF \
    -DFMT_PEDANTIC=ON \
    -DCMAKE_POSITION_INDEPENDENT_CODE=ON \
    -DBUILD_SHARED_LIBS=ON
%cmake_build

%install
%cmake_install

%check

%if 0%{?suse_version} > 1500 || 0%{?sle_version} > 150000
%package -n libfmt11
Summary: Small, safe and fast formatting library for C++

%description -n libfmt11
C++ Format is an open-source formatting library for C++. It can be used
as a safe alternative to printf or as a fast alternative to IOStreams.

%package -n fmt-devel
SUmmary: Development files for fmt

%description -n fmt-devel
This package contains the header file for using fmt.

%post -n libfmt11 -p /sbin/ldconfig
%postun -n libfmt11 -p /sbin/ldconfig

%files -n libfmt11
%license LICENSE
%doc ChangeLog.md README.md
%{_libdir}/libfmt.so.*

%files -n fmt-devel
%{_includedir}/fmt
%{_libdir}/libfmt.so
%{_libdir}/cmake/fmt
%{_libdir}/pkgconfig/fmt.pc
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n fmt
Summary: Small, safe and fast formatting library for C++

%description -n fmt
C++ Format is an open-source formatting library for C++. It can be used
as a safe alternative to printf or as a fast alternative to IOStreams.

%package -n fmt-devel
SUmmary: Development files for fmt

%description -n fmt-devel
This package contains the header file for using fmt.

%post -n fmt -p /sbin/ldconfig
%postun -n fmt -p /sbin/ldconfig

%files -n fmt
%license LICENSE
%doc ChangeLog.md README.md
%{_libdir}/libfmt.so.*

%files -n fmt-devel
%{_includedir}/fmt
%{_libdir}/libfmt.so
%{_libdir}/cmake/fmt
%{_libdir}/pkgconfig/fmt.pc
%endif

%changelog
