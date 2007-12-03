# TODO:
# - do something with jms / jmx requirements;
#   http://lists.pld-linux.org/mailman/pipermail/pld-devel-en/2006-May/017648.html
# - jndi (whatever it is) is required for jmx interface
#
# NOTE:
# - javamail is provided by java-gnu-mail
# - jmx by java-sun-jre

%include	/usr/lib/rpm/macros.java
Summary:	log4j - logging for Java
Summary(pl.UTF-8):	log4j - zapis logów dla Javy
Name:		logging-log4j
Version:	1.2.15
Release:	1
License:	Apache
Group:		Development/Languages/Java
Source0:	http://www.apache.org/dist/logging/log4j/%{version}/apache-log4j-%{version}.tar.gz
# Source0-md5:	10f04abe4d68d5a89e8eb167e4e45e1a
URL:		http://logging.apache.org/log4j/
BuildRequires:	ant
BuildRequires:	java-activation
BuildRequires:	javamail >= 1.2
BuildRequires:	jdk >= 1.2
#BuildRequires:	jms
#BuildRequires:	jmx
BuildRequires:	jpackage-utils
BuildRequires:	junit >= 3.8
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	javamail >= 1.2
Requires:	jdk >= 1.2
#Requires:	jms
#Requires:	junit
Provides:	log4j = %{version}
Obsoletes:	jakarta-log4j
BuildArch:	noarch
ExclusiveArch:	i586 i686 pentium3 pentium4 athlon %{x8664} noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
With log4j it is possible to enable logging at runtime without
modifying the application binary.

%description -l pl.UTF-8
Przy użyciu log4j można włączyć zapis do logów przy uruchamianiu bez
modyfikowania binarnej aplikacji.

%package doc
Summary:	Online manual for log4j
Summary(pl.UTF-8):	Dokumentacja online do log4j
Group:		Documentation
Obsoletes:	jakarta-log4j-doc

%description doc
Online manual for log4j.

%description doc -l pl.UTF-8
Dokumentacja online do log4j.

%package javadoc
Summary:	API documentation for log4j
Summary(pl.UTF-8):	Dokumentacja API log4j
Group:		Documentation
Requires:	jpackage-utils
Obsoletes:	jakarta-log4j-doc

%description javadoc
API documentation for log4j.

%description javadoc -l pl.UTF-8
Dokumentacja API log4j.

%prep
%setup -q -n apache-log4j-%{version}

%build
required_jars="mailapi activation junit"
export CLASSPATH=$(build-classpath $required_jars)
%ant jar javadoc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_javadir},%{_javadocdir}/%{name}-%{version}}
cp -a dist/lib/log4j-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/log4j-%{version}.jar
ln -s log4j-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/log4j.jar

cp -a docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE
%{_javadir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc site/{apidocs,css,images,xref,xref-test,*.html}

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}
