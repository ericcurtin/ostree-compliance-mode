Name:          ostree-compliance-mode
Version:       0.2
Release:       2%{?dist}
Summary:       Leaves the system in a modifiable state in compliance with GPLv3

License:       GPLv2
URL:           https://github.com/ericcurtin/%{name}
Source0:       %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc

Requires:      ostree
Requires:      python3
Requires:      rpm-ostree

%description
%{summary}.

%prep
%autosetup

%build
${CC} ${RPM_OPT_FLAGS} -Wall -Winvalid-pch -Wextra -Wpedantic -Werror -std=gnu11 -Wstrict-aliasing -Wchar-subscripts -Wformat-security -Wmissing-declarations -Wpointer-arith -Wshadow -Wsign-compare -Wtype-limits -Wunused-function ostree-compliance-mode.c -o ostree-compliance-mode

%install
currently_deployed_ref=$(rpm-ostree status --json |  python3 -c "import sys, json; print(json.load(sys.stdin)['deployments'],[$1] ,['origin'])")

install -Dm 600 <(echo "$currently_deployed_ref") %{buildroot}%{_sysconfdir}/ostree-compliance-mode.conf
install -Dm 4411 ostree-compliance-mode %{buildroot}%{_bindir}/ostree-compliance-mode
install -Dm 500 %{SOURCE0} %{buildroot}%{_libexecdir}/ostree-compliance-mode-helper

%files
%license LICENSE
%doc README.md
%{_sysconfdir}/ostree-compliance-mode.conf
%{_bindir}/ostree-compliance-mode
%{_libexecdir}/ostree-compliance-mode-helper

%changelog
* Wed Sep 21 2022 Ian Mullins <imullins@redhat.com> - 0.2-2
- Populate ostree-compliance-mode.conf file with relevant rpm-ostree status

* Mon Sep 12 2022 Ian Mullins <imullins@redhat.com> - 0.2-1
- Initial version
