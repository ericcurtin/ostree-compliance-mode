Name:           ostree-compliance-mode
Version:        0.1
Release:        1%{?dist}
Summary:        ostree-compliance-mode is a tool designed to purge protected data, leaving the system in a modifyable state in compliance with GPLv3

License:        GPLv2
URL:            https://github.com/ericcurtin/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: meson
BuildRequires: gcc

Requires:      ostree
Requires:      rpm-ostree
Requires:      python3

%description
%{summary}

%prep
%autosetup
%global debug_package %{nil}

%build
%meson
%meson_build

%check
%meson_test

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libexecdir}
install -m 4411 %{SOURCE0} %{buildroot}%{_bindir}/ostree-compliance-mode
install -m 500 %{SOURCE0} %{buildroot}%{_libexecdir}/ostree-compliance-mode-helper

%files
%license LICENSE
%doc README.md
%{_bindir}/ostree-compliance-mode
%{_libexecdir}/ostree-compliance-mode-helper

%changelog
* Fri Sep 9 2022 Ian Mullins <imullins@redhat.com> - 0.1-1
- ostree-compliance-mode
