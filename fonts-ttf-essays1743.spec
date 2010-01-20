Summary:	A small collection of Truetype fonts
Name:		fonts-ttf-essays1743
Version:	1.0
Release:	%mkrel 7

Source0:	Essays1743-1.0-ttf.tar.gz
Source1:	Isabella.ttf.tar.gz
Source2:	StayPuft.ttf.tar.gz
License:	GPL/LGPL
Group:		System/Fonts/True type
URL:		http://www.thibault.org/fonts/
BuildRoot:	%_tmppath/%name-%version-%release-root
BuildArch:	noarch
BuildRequires:	fontconfig
BuildRequires:	freetype-tools


%description 
A small collection of Truetype fonts.

This package contains 3 fonts:
 * Essays1743 which is based on the typeface used in a 1743
   English translation of Montaigne's Essays,
 * Isabella is based on the calligraphic hand used in the Isabella
   Breviary, made around 1497, in Holland, for Isabella of Castille,
   the first queen of united Spain,
 * StayPuft is a rounded, sort of marshmallowy font.
   It's kind of cute, and might be good for frivolous stuff such as
   birthday cards.


%prep
%setup -q -b1 -b2 -c %name-%version

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/fonts/ttf/essays1743

cp -f *.ttf $RPM_BUILD_ROOT%{_datadir}/fonts/ttf/essays1743/
cp -f Isabella/*.ttf $RPM_BUILD_ROOT%{_datadir}/fonts/ttf/essays1743/
cp -f Essays1743/*.ttf $RPM_BUILD_ROOT%{_datadir}/fonts/ttf/essays1743/

{
    pushd $RPM_BUILD_ROOT/usr/share/fonts/ttf/essays1743
    ttmkfdir > fonts.dir
    cp fonts.dir fonts.scale
    popd
}
# Rename docs
cp README.txt StayPuft.README.txt
cp Isabella/README.txt Isabella/Isabella.README.txt
cp Essays1743/README Essays1743/Essays1743.README.txt

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/fonts/ttf/essays1743 \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-essays:pri=50

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644,root,root,0755)
%doc StayPuft.README.txt Isabella/Isabella.README.txt Essays1743/Essays1743.README.txt
%dir %_datadir/fonts/ttf/essays1743
%config(noreplace) %{_datadir}/fonts/ttf/essays1743/fonts.dir
%config(noreplace) %{_datadir}/fonts/ttf/essays1743/fonts.scale
%{_datadir}/fonts/ttf/essays1743/*.ttf
%{_sysconfdir}/X11/fontpath.d/ttf-essays:pri=50
