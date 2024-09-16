Name:           netflow2ng
Version:        x.y.z
Release:        1%{?dist}
Summary:        A lightweight NetFlow collector and parser
License:        MIT
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc, make
Requires:       libpcap

%description
netflow2ng is a lightweight NetFlow collector and parser.

%define bin_path %{_builddir}/netflow2ng/dist/netflow2ng-0.0.5

%global debug_package %{nil}

%prep
%autosetup -n %{name}

%build
make

%install
mkdir -p %{buildroot}/usr/local/bin
install -m 0755 %{bin_path} %{buildroot}/usr/local/bin/%{name}

%files
/usr/local/bin/netflow2ng

%changelog
* Thu Oct 19 2023 Your Name <youremail@example.com> - 0.0.5-1
- Initial RPM release

