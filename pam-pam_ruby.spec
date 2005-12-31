%define		rubypamversion	1.5.0
%define		modulename	pam_ruby
Summary:	PAM module to authenticate via a Ruby script
Summary(pl):	Modu³ PAM do uwierzytelniania z u¿yciem skryptu w jêzyku Ruby
Name:		pam-%{modulename}
Version:	1.3.1
Release:	4
Epoch:		1
License:	GPL
Group:		Development/Languages
Source0:	http://dl.sourceforge.net/ruby-pam/pam-ruby-%{version}.tar.gz
# Source0-md5:	2b6b3442d8f47ce84a6368eb5fa7fa54
Source1:	http://dl.sourceforge.net/ruby-pam/ruby-pam-%{rubypamversion}.tar.gz
# Source1-md5:	a6437f94621811cda255c69d6bb3a673
Patch0:		%{name}-libdir.patch
URL:		http://ruby-pam.sourceforge.net/pam-ruby.html
BuildRequires:	autoconf
BuildRequires:	pam-devel
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
Requires:	pam
Requires:	ruby-PAM = %{rubypamversion}
Obsoletes:	pam-ruby
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PAM/Ruby is a PAM module for writing the PAM authentication module
with the Ruby.

%description -l pl
PAM/Ruby to modu³ PAM umo¿liwiaj±cy pisanie modu³u uwierzytelniaj±cego
PAM w jêzyku Ruby.

%prep
%setup -q -n pam-ruby-%{version} -a 1
%patch0 -p0

%build
%{__autoconf}
%configure \
	--with-ruby-pam=ruby-pam-%{rubypamversion} \
	--with-instdir=/%{_lib}/security

%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_lib}/security

install pam_ruby.so $RPM_BUILD_ROOT/%{_lib}/security

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README README.html sample
%attr(755,root,root) /%{_lib}/security/*.so
