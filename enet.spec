%define major 2
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Simple and robust network communication layer on top of UDP
Name:		enet
Version:	1.3.9
Release:	1
Source0:	http://enet.bespin.org/download/%{name}-%{version}.tar.gz
License:	BSD
Group:		System/Libraries
URL:		http://enet.bespin.org

%description
ENet's purpose is to provide a relatively thin, simple and robust
network communication layer on top of UDP (User Datagram Protocol). The
primary feature it provides is optional reliable, in-order delivery of
packets.

ENet omits certain higher level networking features such as
authentication, lobbying, server discovery, encryption, or other similar
tasks that are particularly application specific so that the library
remains flexible, portable, and easily embeddable.

%package -n	%{libname}
Summary:	Libraries for %{name}
Group:		System/Libraries

%description -n	%{libname}
ENet's purpose is to provide a relatively thin, simple and robust
network communication layer on top of UDP (User Datagram Protocol). The
primary feature it provides is optional reliable, in-order delivery of
packets.

ENet omits certain higher level networking features such as
authentication, lobbying, server discovery, encryption, or other similar
tasks that are particularly application specific so that the library
remains flexible, portable, and easily embeddable.

This package provides the libraries for %{name}.

%package -n %{develname}
Summary:	Development files for for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n	%{develname}
Development files and headers for %{name}.

%prep
%setup -q 

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

# we don't want	these
rm -rf %{buildroot}%{_libdir}/*.la

%files -n %{libname}
%{_libdir}/libenet.so.%{major}*

%files -n %{develname}
%doc LICENSE README ChangeLog
%{_includedir}/%{name}
%{_libdir}/libenet.so
%{_libdir}/pkgconfig/libenet.pc

