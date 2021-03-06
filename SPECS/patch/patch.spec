Summary:	Program for modifying or creating files
Name:		patch
Version:	2.7.5
Release:	3%{?dist}
License:	GPLv3+
URL:		http://www.gnu.org/software/%{name}
Source0:	ftp://ftp.gnu.org/gnu/patch/%{name}-%{version}.tar.gz
%define sha1 patch=04d23f6e48e95efb07d12ccf44d1f35fb210f457
Group:		Development/Tools
Vendor:		VMware, Inc.
Distribution: 	Photon
%description
Program for modifying or creating files by applying a patch
file typically created by the diff program.
%prep
%setup -q
%build
./configure \
	--prefix=%{_prefix} \
	--disable-silent-rules
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%check
make  %{?_smp_mflags} check
%files
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/*/*
%changelog
*       Fri Oct 07 2016 ChangLee <changlee@vmware.com> 2.7.5-3
-       Modified %check
*	Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 2.7.5-2
-	GA - Bump release of all rpms
*	Tue Aug 11 2015 Divya Thaluru <dthaluru@vmware.com> 2.7.5-1
-	Updating to 2.7.5 version
*	Wed Nov 5 2014 Divya Thaluru <dthaluru@vmware.com> 2.7.1-1
-	Initial build. First version
