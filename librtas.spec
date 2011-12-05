Summary: Libraries to provide access to RTAS calls and RTAS events
Name:    librtas
Version: 1.3.4
Release: 2%{?dist}
URL:     http://librtas.ozlabs.org
License: CPL
Group:   System Environment/Libraries

Source: http://librtas.ozlabs.org/releases/%{name}-%{version}.tar.gz

Patch0: %{name}-1.3.4-libdir.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
ExclusiveArch: ppc ppc64

Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
The librtas shared library provides userspace with an interface
through which certain RTAS calls can be made.  The library uses
either of the RTAS User Module or the RTAS system call to direct
the kernel in making these calls.

The librtasevent shared library provides users with a set of
definitions and common routines useful in parsing and dumping
the contents of RTAS events.

%package devel
Summary:  C header files for development with librtas
Group:    Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
The librtas-devel packages contains the header files necessary for
developing programs using librtas.

%prep
%setup
%patch0 -p1 -b .libdir

%build
%{__make} CFLAGS="%{optflags} -fPIC -DPIC -I." %{?_smp_mflags}

%install
mkdir -p %{buildroot}/%{_libdir}
%{__make} install DESTDIR=%{buildroot} LIB_DIR=%{_libdir}
%{__rm} -rf %{buildroot}%{_datadir}/doc

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYRIGHT README Changelog
%{_libdir}/librtas.so.%{version}
%{_libdir}/librtasevent.so.%{version}
%{_libdir}/libofdt.so.%{version}

%files devel
%defattr(-,root,root,-)
%{_libdir}/librtas.so
%{_libdir}/librtasevent.so
%{_includedir}/librtas.h
%{_includedir}/librtasevent.h
%{_includedir}/librtasevent_v4.h
%{_includedir}/librtasevent_v6.h
%{_includedir}/common.h
%{_includedir}/libofdt.h
%{_libdir}/libofdt.so

%changelog
* Thu Feb 25 2010 Roman Rakus <rrakus@redhat.com> - 1.3.4-2
- Use right license (CPL)

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.3.4-1.1
- Rebuilt for RHEL 6

* Mon Sep 21 2009 Roman Rakus <rrakus@redhat.com> - 1.3.4-1
- Upstream release 1.3.4

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 08 2008 David Cantrell <dcantrell@redhat.com> - 1.3.3-3
- Rebuild for gcc-4.3

* Tue Dec 18 2007 David Cantrell <dcantrell@redhat.com> - 1.3.3-2
- Spec cleanups

* Tue Dec 18 2007 David Cantrell <dcantrell@redhat.com> - 1.3.3-1
- Upgraded to librtas-1.3.3 (#253522)

* Mon Sep 10 2007 David Cantrell <dcantrell@redhat.com> - 1.3.2-1
- Upgraded to librtas-1.3.2
- Cleaned up spec file to conform to Fedora packaging guidelines

* Tue Aug 21 2007 David Cantrell <dcantrell@redhat.com> - 1.2.4-4
- Rebuild

* Sat Mar 31 2007 David Woodhouse <dwmw2@redhat.com> - 1.2.4-3
- Install libraries into /usr/lib64 on PPC64.

* Tue Aug 01 2006 Paul Nasrat <pnasrat@redhat.com> - 1.2.4-2
- Backport syscall fix from upstream 

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.2.4-1.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.2.4-1.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.2.4-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Nov 03 2005 Paul Nasrat <pnasrat@redhat.com> 1.2.4-1
- Update to latest version

* Thu Nov 03 2005 Paul Nasrat <pnasrat@redhat.com> 1.2.2-1
- Initial release
