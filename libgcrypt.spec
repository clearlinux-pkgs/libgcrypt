#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x249B39D24F25E3B6 (dshaw@jabberwocky.com)
#
Name     : libgcrypt
Version  : 1.8.2
Release  : 28
URL      : ftp://ftp.gnupg.org/gcrypt/libgcrypt/libgcrypt-1.8.2.tar.gz
Source0  : ftp://ftp.gnupg.org/gcrypt/libgcrypt/libgcrypt-1.8.2.tar.gz
Source99 : ftp://ftp.gnupg.org/gcrypt/libgcrypt/libgcrypt-1.8.2.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 LGPL-2.0+ LGPL-2.1
Requires: libgcrypt-bin
Requires: libgcrypt-lib
Requires: libgcrypt-doc
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : libgpg-error-dev
BuildRequires : libgpg-error-dev32

%description
Libgcrypt - The GNU Crypto Library
------------------------------------
Version 1.7

%package bin
Summary: bin components for the libgcrypt package.
Group: Binaries

%description bin
bin components for the libgcrypt package.


%package dev
Summary: dev components for the libgcrypt package.
Group: Development
Requires: libgcrypt-lib
Requires: libgcrypt-bin
Provides: libgcrypt-devel

%description dev
dev components for the libgcrypt package.


%package dev32
Summary: dev32 components for the libgcrypt package.
Group: Default
Requires: libgcrypt-lib32
Requires: libgcrypt-bin
Requires: libgcrypt-dev

%description dev32
dev32 components for the libgcrypt package.


%package doc
Summary: doc components for the libgcrypt package.
Group: Documentation

%description doc
doc components for the libgcrypt package.


%package lib
Summary: lib components for the libgcrypt package.
Group: Libraries

%description lib
lib components for the libgcrypt package.


%package lib32
Summary: lib32 components for the libgcrypt package.
Group: Default

%description lib32
lib32 components for the libgcrypt package.


%prep
%setup -q -n libgcrypt-1.8.2
pushd ..
cp -a libgcrypt-1.8.2 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1513200003
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%configure --disable-static --enable-ciphers="cast5 aes twofish serpent rfc2268 seed camellia idea salsa20 gost28147 chacha20" --disable-large-data-tests
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static --enable-ciphers="cast5 aes twofish serpent rfc2268 seed camellia idea salsa20 gost28147 chacha20" --disable-large-data-tests   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%install
export SOURCE_DATE_EPOCH=1513200003
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/dumpsexp
/usr/bin/hmac256
/usr/bin/libgcrypt-config
/usr/bin/mpicalc

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libgcrypt.so
/usr/share/aclocal/*.m4

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libgcrypt.so

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgcrypt.so.20
/usr/lib64/libgcrypt.so.20.2.2

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libgcrypt.so.20
/usr/lib32/libgcrypt.so.20.2.2
