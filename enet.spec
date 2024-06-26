%define major		7
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Summary:	Simple and robust network communication layer on top of UDP

Name:		enet
Version:	1.3.18
Release:	1
Source0:	https://enet.bespin.org/download/%{name}-%{version}.tar.gz
Source100:	enet.rpmlintrc
License:	BSD
Group:		System/Libraries
URL:		https://enet.bespin.org

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
%configure --disable-static
%make_build

%install
%make_install

%files -n %{libname}
%doc LICENSE README ChangeLog
%{_libdir}/libenet.so.%{major}*

%files -n %{develname}
%{_includedir}/%{name}
%{_libdir}/libenet.so
%{_libdir}/pkgconfig/libenet.pc
