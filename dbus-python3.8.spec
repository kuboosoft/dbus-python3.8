%global python3dir %{_builddir}/python3-%{name}-%{version}-%{release}
%define _legacy_common_support 1

Summary: D-Bus Python Bindings
Name:    dbus-python3.8
Version: 1.2.16
Release: 6%{?dist}

License: MIT
URL:     http://www.freedesktop.org/wiki/Software/DBusBindings/
Source0: http://dbus.freedesktop.org/releases/dbus-python/dbus-python-%{version}.tar.gz

# borrow centos7 patch to use sitearch properly
Patch0: 0001-Move-python-modules-to-architecture-specific-directo.patch


BuildRequires: python3.8-devel
BuildRequires: dbus-devel
BuildRequires: dbus-glib-devel
# autoreconf and friends
BuildRequires: autoconf-archive automake libtool

%global _description\
D-Bus python bindings for use with python programs.

%description %_description


%prep
%autosetup -n dbus-python-%{version}

# For new arches (aarch64/ppc64le), and patch0
autoreconf -vif


%build
%set_build_flags
%configure PYTHON=/usr/bin/python3.8 PYTHON_VERSION=3.8
sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0/g' libtool
%make_build

%install
%make_install
rm -fv  $RPM_BUILD_ROOT%{_libdir}/python3.8/site-packages/*.la

%files 
%doc NEWS
%license COPYING
%{_libdir}/python3.8/site-packages/_dbus_bindings.so
%{_libdir}/python3.8/site-packages/_dbus_glib_bindings.so
%{_libdir}/python3.8/site-packages/dbus/
%exclude %{_includedir}/dbus-1.0/dbus/dbus-python.h
%exclude %{_libdir}/pkgconfig/dbus-python.pc

%changelog
