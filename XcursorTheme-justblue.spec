%define		_name justblue
Summary:	X11 cursor theme - justblue
Summary(pl):	Notyw kursorów dla X11 - justblue
Name:		XcursorTheme-%{_name}
Version:	0.21
Release:	1
License:	Artistic 2.0
Group:		Themes
Source0:	http://www.kde-look.org/content/files/10163-%{_name}-%{version}.tar.bz2
# Source0-md5:	63a1e9832e4f9a3620e3eb04a63a758b
URL:		http://www.kde-look.org/content/show.php?content=10163
BuildRequires:	XFree86 >= 4.3
BuildArch:	noarch
Requires:	XFree86 >= 4.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A gradiented, blue/gray cursor theme.

%description -l pl
Niebiesko-szary motyw kursorów z gradientem.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iconsdir}
%{__tar} xfj %{SOURCE0} -C $RPM_BUILD_ROOT%{_iconsdir}/
mv -f  $RPM_BUILD_ROOT%{_iconsdir}/%{_name}{-%{version},}
rm -rf $RPM_BUILD_ROOT%{_iconsdir}/%{_name}/{*.sh,sshot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_iconsdir}/%{_name}
