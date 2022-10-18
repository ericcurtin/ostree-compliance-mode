Name:          ostree-compliance-mode
Version:       0.2
Release:       3%{?dist}
Summary:       Leaves the system in a modifiable state in compliance with GPLv3

License:       GPLv2
URL:           https://github.com/ericcurtin/%{name}
Source0:       %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc

Requires:      ostree
Requires:      rpm-ostree
Requires:      python

%description
%{summary}.

%prep
%autosetup

%build
%set_build_flags
${CC} ${RPM_OPT_FLAGS} -Wall -Winvalid-pch -Wextra -Wpedantic -Werror -std=gnu11 -Wstrict-aliasing -Wchar-subscripts -Wformat-security -Wmissing-declarations -Wpointer-arith -Wshadow -Wsign-compare -Wtype-limits -Wunused-function ostree-compliance-mode.c -o ostree-compliance-mode

%install
install -Dm 4411 ostree-compliance-mode %{buildroot}%{_bindir}/ostree-compliance-mode
install -Dm 500 ostree-compliance-mode-helper %{buildroot}%{_libexecdir}/ostree-compliance-mode-helper
install -Dm 600 <("") %{buildroot}%{_sysconfdir}/ostree-compliance-mode.conf

%files
%license LICENSE
%doc README.md
%{_bindir}/ostree-compliance-mode
%{_libexecdir}/ostree-compliance-mode-helper
%{_sysconfdir}/ostree-compliance-mode.conf

%changelog
* Thu Oct 20 2022 Ian Mullins <imullins@redhat.com> - 0.2-3
- Ship an empty ostree-compliance-mode.conf file. This way permissions are set
  correctly and it's SELinux file context is set correctly.

* Fri Oct 14 2022 Ian Mullins <imullins@redhat.com> - 0.2-2
- Minor changes to install and build section to correctly install required files

* Mon Sep 12 2022 Ian Mullins <imullins@redhat.com> - 0.2-1
- Initial version
