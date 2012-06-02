%global fontname junicode
%global fontconf 65-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        1.01
Release:        5%{?dist}
Summary:        JUnicode fonts

Group:          User Interface/X
License:        OFL
URL:            http://junicode.sourceforge.net/
Source0:        http://junicode.cvs.sourceforge.net/viewvc/junicode/junicode/src/Junicode-Regular.sfd
Source1:       http://junicode.cvs.sourceforge.net/viewvc/junicode/junicode/src/Junicode-Bold.sfd
Source2:        http://junicode.cvs.sourceforge.net/viewvc/junicode/junicode/src/Junicode-Italic.sfd
Source3:        %{name}-fontconfig.conf
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildArch:      noarch
BuildRequires:  fontpackages-devel
BuildRequires:  fontforge
Requires:       fontpackages-filesystem


%description
The Junicode font is designed to meet the needs of medieval scholars; however, it has a large enough character set to be useful to the general user. It comes in Regular, Italic, Bold and Bold Italic faces. The Regular face has the fullest character set, and is richest in OpenType features. 

%prep

%build
fontforge -lang=ff -script "-" %{SOURCE0} <<_EOF
i = 1
while ( i < \$argc )
  Open (\$argv[i], 1)
  Generate (\$fontname + ".ttf")
  PrintSetup (5)
  PrintFont (0, 0, "", \$fontname + "-sample.pdf")
  Close()
  i++
endloop
_EOF

%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

%clean
rm -fr %{buildroot}

%_font_pkg -f %{fontconf} *.ttf
%doc *.pdf

%changelog

* Sat Jun 02 2012 Prathamesh Sonpatki <csonpatki@gmail,com> - 1.009-1
- Initial package for fedora
