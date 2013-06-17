Summary:	Tcl Library for Interacting with DBus
Name:		tcl-dbus
Version:	1.1
Release:	1
License:	BSD
Group:		Development/Languages/Tcl
URL:		http://dbus-tcl.sourceforge.net/
Source0:	http://downloads.sourceforge.net/dbus-tcl/dbus-tcl%{version}.tar.gz
# Source0-md5:	370b15f2e88983934574e49b16fc39bc
BuildRequires:	dbus-devel
BuildRequires:	pkg-config
BuildRequires:	tcl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBus-Tcl is a Tcl library for interacting with the DBus, a popular
system for applications to talk to eachother. DBus can also be used to
coordinate the lifecycle of a process. For more information about
DBus, see http://www.freedesktop.org/wiki/Software/dbus

%prep
%setup -q -n dbus-tcl%{version}

%build

%configure \
%if "%{_lib}" == "lib64"
	--enable-64bit \
%endif
	--enable-threads

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/dbus-tcl
%attr(755,root,root) %{_libdir}/dbus-tcl/libdbus-tcl%{version}.so
%{_libdir}/dbus-tcl/pkgIndex.tcl
