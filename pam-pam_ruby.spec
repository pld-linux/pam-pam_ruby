%define	ruby_sitearchdir	%(ruby -r rbconfig -e 'print Config::CONFIG["sitearchdir"]')
%define	rubypamversion	1.5.0
Summary:	PAM module to authenticate via a ruby script
Name:		pam-pam_ruby
Version:	1.3.1
Release:	1
Epoch:		1
License:	GPL
Group:		Development/Languages
Source0:	http://dl.sourceforge.net/ruby-pam/pam-ruby-%{version}.tar.gz
# Source0-md5:	2b6b3442d8f47ce84a6368eb5fa7fa54
Source1:	http://dl.sourceforge.net/ruby-pam/ruby-pam-%{rubypamversion}.tar.gz
# Source1-md5:	a6437f94621811cda255c69d6bb3a673
URL:		http://ruby-pam.sourceforge.net/pam-ruby.html
BuildRequires:	pam-devel
BuildRequires:	ruby
Requires:	ruby
Requires: ruby-pam = %{rubypamversion}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PAM module to authenticate via a ruby script

%prep
%setup -q -a 1

%build
%{__autoconf}
%configure --with-ruby-pam=ruby-pam-1.5.0
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/security

install pam_ruby.so $RPM_BUILD_ROOT/lib/security

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README README.html sample
%attr(755,root,root) /lib/security/*.so
