Name:       jsontool
Summary:    Tool for json file validation, merging, modification, filtering etc.
Version:    9.0.3
Release:    0
Group:      Tools
License:    MIT
Source0:    %{name}-%{version}.tar.gz
BuildRequires: nodejs
Requires:   nodejs

%description
Tool for json file validation, merging, modification, filtering etc.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/%{_prefix}/bin
install json %{buildroot}/%{_prefix}/bin

%files
%defattr(-,root,root,-)
%{_prefix}/bin/*
