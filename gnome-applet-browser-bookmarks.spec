%define		_realname	browser-bookmarks-menu
Summary:	Small applet to allow easy access to bookmarks
Summary(pl):	Ma�y aplet umo�liwiaj�cy �atwy dost�p do zak�adek
Name:		gnome-applet-browser-bookmarks
Version:	0.3
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/browserbookapp/%{_realname}-%{version}.tar.gz
# Source0-md5:	9af490f32e1651f682984f69d2299955
URL:		http://browserbookapp.sourceforge.net/
BuildRequires:	sed >= 4.0
Requires:	python-gnome-applet
Requires:	python-gnome-gconf
Requires:	python-gnome-ui
Requires:	python-libxml2
Requires(post):	GConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appletdirname		%{_datadir}/browser-bookmarks-applet

%description
This is a small GNOME applet to allow easy access to your browser's
bookmarks, even when your browser is not open. It supports Mozilla,
Mozilla Firefox, Epiphany, Galeon and Konqueror bookmarks.

%description -l pl
Ma�y aplet GNOME umo�liwiaj�cy �atwy dost�p do zak�adek, nawet gdy
przegl�darka WWW nie jest uruchomiona. Obs�ugiwane przegl�darki to:
Mozilla, Mozilla Firefox, Epiphany, Galeon i Konqueror.

%prep
%setup -q -n %{_realname}-%{version}

%build
sed -i -e "s:%{_prefix}/libexec:%{_appletdirname}:" BrowserBookmarksMenu.server

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_appletdirname},%{_libdir}/bonobo/servers}
install BrowserBookmarksMenu.server $RPM_BUILD_ROOT%{_libdir}/bonobo/servers
install browser-bookmarks-menu.py $RPM_BUILD_ROOT%{_appletdirname}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install

%files
%defattr(644,root,root,755)
%doc CHANGELOG
%attr(755,root,root) %{_appletdirname}
%{_libdir}/bonobo/servers/*.server
