%define		_realname	browser-bookmarks-menu
Summary:	Small applet to allow easy access to bookmarks
Summary(pl.UTF-8):	Mały aplet umożliwiający łatwy dostęp do zakładek
Name:		gnome-applet-browser-bookmarks
Version:	0.6
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/browserbookapp/%{_realname}-%{version}.tar.gz
# Source0-md5:	e9f312503d56a291a820911483c6507d
URL:		http://browserbookapp.sourceforge.net/
BuildRequires:	sed >= 4.0
Requires:	python-gnome-applet
Requires:	python-gnome-gconf
Requires:	python-gnome-ui
Requires:	python-gnome-vfs
Requires:	python-pygtk-gtk >= 2:2.6.0
Requires:	python-libxml2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appletdirname		%{_datadir}/browser-bookmarks-applet

%description
This is a small GNOME applet to allow easy access to your browser's
bookmarks, even when your browser is not open. It supports Mozilla,
Mozilla Firefox, Epiphany, Galeon and Konqueror bookmarks.

%description -l pl.UTF-8
Mały aplet GNOME umożliwiający łatwy dostęp do zakładek, nawet gdy
przeglądarka WWW nie jest uruchomiona. Obsługiwane przeglądarki to:
Mozilla, Mozilla Firefox, Epiphany, Galeon i Konqueror.

%prep
%setup -q -n %{_realname}-%{version}

%build
sed -i -e "s:/usr/lib/%{_realname}:%{_appletdirname}:" BrowserBookmarksMenu.server

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_appletdirname},%{_libdir}/bonobo/servers}
install BrowserBookmarksMenu.server $RPM_BUILD_ROOT%{_libdir}/bonobo/servers
install browser-bookmarks-menu.py $RPM_BUILD_ROOT%{_appletdirname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG
%attr(755,root,root) %{_appletdirname}
%{_libdir}/bonobo/servers/*.server
