Name:           msmtp
Version:        1.8.26
Release:        1%{?dist}
Summary:        An SMTP client

License:        GPLv3+
URL:            https://marlam.de/msmtp/
Source0:        %{name}-%{version}.tar.xz

BuildRequires:  make, gcc, openssl-devel, libidn-devel
Requires:       ca-certificates

%define _local_etcdir /usr/local/etc

%description
msmtp is an SMTP client that can be used as an "SMTP plugin" for Mutt and other mail user agents.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# Create the /etc/ directory
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}

# Create the /usr/local/etc directory and a default configuration file
mkdir -p $RPM_BUILD_ROOT%{_local_etcdir}
echo "defaults" > $RPM_BUILD_ROOT%{_local_etcdir}/msmtprc

# Copy to etc
cp -a $RPM_BUILD_ROOT%{_local_etcdir}/msmtprc $RPM_BUILD_ROOT%{_sysconfdir}/msmtprc

%files
%doc README
%{_bindir}/msmtp
%{_bindir}/msmtpd
%{_mandir}/man1/msmtp.1.gz
%{_mandir}/man1/msmtpd.1.gz
%{_sysconfdir}/msmtprc
%{_local_etcdir}/msmtprc

# Locale files
%{_datadir}/locale/de/LC_MESSAGES/msmtp.mo
%{_datadir}/locale/eo/LC_MESSAGES/msmtp.mo
%{_datadir}/locale/fr/LC_MESSAGES/msmtp.mo
%{_datadir}/locale/pt_BR/LC_MESSAGES/msmtp.mo
%{_datadir}/locale/ro/LC_MESSAGES/msmtp.mo
%{_datadir}/locale/ru/LC_MESSAGES/msmtp.mo
%{_datadir}/locale/sr/LC_MESSAGES/msmtp.mo
%{_datadir}/locale/sv/LC_MESSAGES/msmtp.mo
%{_datadir}/locale/ta/LC_MESSAGES/msmtp.mo
%{_datadir}/locale/uk/LC_MESSAGES/msmtp.mo

# Info files
%{_infodir}/dir
%{_infodir}/msmtp.info.gz

%changelog
* Fri Aug 09 2024 sefa <1sefatuter@gmail.com> - 1.8.26-1
- Initial package
