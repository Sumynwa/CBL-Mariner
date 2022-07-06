Name:           python3-geomet
Version:        0.2.1
Release:        1%{?dist}
Summary:        GeoJSON <-> WKT/WKB conversion utilities
License:        ASL 2.0
Vendor:         Microsoft Corporation
Distribution:   Mariner
Group:          Development/Languages/Python
Url:            https://github.com/geomet
Source0:        https://github.com/geomet/geomet/archive/refs/tags/%{version}.tar.gz#/geomet-%{version}.tar.gz
BuildRequires:  python3
BuildRequires:  python3-libs
BuildRequires:  python3-setuptools
Requires:       python3
Requires:       python3-libs
Requires:       python3-six
Requires:       python3-click
Requires:       python3-setuptools

BuildArch:      noarch

%description
Convert GeoJSON to WKT/WKB (Well-Known Text/Binary), and vice versa.

%prep
%autosetup -n geomet-%{version}

%build
%py3_build

%install
%py3_install
# Remove /usr/LICENSE file which is being copied during install_data
rm -f %{buildroot}/%{_exec_prefix}/LICENSE

%check
%python3 setup.py test

%files
%defattr(-,root,root,-)
%license LICENSE
%{_bindir}/geomet
%{python3_sitelib}/*

%changelog
*   Wed Jun 22 2022 Sumedh Sharma <sumsharma@microsoft.com> - 0.2.1-1
-   Initial CBL-Mariner import from PhotonOS (license: ASL 2.0)
-   Bumping version to 0.2.1
-   Adding as run dependency for python-cassandra-driver needed by cassandra-medusa.
-   License Verified.

*   Fri Jun 11 2021 Ankit Jain <ankitja@vmware.com> 0.1.2-1
-   Initial packaging for Photon
