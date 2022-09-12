Name:          ostree-compliance-mode
Version:       0.2
Release:       1%{?dist}
Summary:       Leaves the system in a modifiable state in compliance with GPLv3

License:       GPLv2
URL:           https://github.com/ericcurtin/%{name}
Source0:       %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc

Requires:      ostree
Requires:      rpm-ostree
Requires:      python3


%description
%{summary}.

%prep
%autosetup

%build
${CC} ${RPM_OPT_FLAGS} -Wall -Winvalid-pch -Wextra -Wpedantic -Werror -std=gnu11 -Wstrict-aliasing -Wchar-subscripts -Wformat-security -Wmissing-declarations -Wpointer-arith -Wshadow -Wsign-compare -Wtype-limits -Wunused-function ostree-compliance-mode.c -o ostree-compliance-mode

%install
install -Dm 4411 ostree-compliance-mode %{buildroot}%{_bindir}/ostree-compliance-mode
install -Dm 500 %{SOURCE0} %{buildroot}%{_libexecdir}/ostree-compliance-mode-helper

%files
%license LICENSE
%doc README.md
%{_bindir}/ostree-compliance-mode
%{_libexecdir}/ostree-compliance-mode-helper

%changelog
* Mon Sep 12 2022 Ian Mullins <imullins@redhat.com> - 0.2-1
- Initial version