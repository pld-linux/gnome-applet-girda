
%define _orig_name girda_applet

Summary:	GNOME IrDA monitor
Summary(es):	Monitador de IrDA para GNOME
Summary(pl):	Monitor IrDA dla GNOME
Name:		gnome-applet-girda
Version:	2.0.3
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/girda/%{_orig_name}-%{version}.tar.gz
# Source0-md5:	b0a7bb78dfaa0a9b94bc7956fcdd1070
URL:		http://sourceforge.net/projects/girda/
BuildRequires:	gnome-panel-devel >= 2.0.0
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	libglade2-devel >= 1:2.0.0
BuildRequires:	libgnome-devel >= 2.0.0
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	libgtop-devel >= 1:2.0.0
BuildRequires:	libwnck-devel >= 0.13
BuildRequires:	scrollkeeper >= 1:0.3.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME IrDA Monitor is a GNOME applet. The applet is monitoring the Ir
port and lists Ir devices in range.

%description -l es
El monitor de IrDA es un applet de GNOME. Este applet monitora el
puerto Ir y lista los equipos Ir en la cobertura.

%description -l pl
Monitor IrD-y jest apletem GNOME. Ten aplet monitoruje porty Ir i
wypisuje urz±dzenia Ir w zasiêgu.

%prep
%setup -q -n %{_orig_name}-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README TODO AUTHORS NEWS
%attr(755,root,root) %{_bindir}/*
%{_libdir}/bonobo/servers/*.server
%{_datadir}/%{_orig_name}
%{_datadir}/gnome-2.0/ui/*.xml
%{_omf_dest_dir}/%{_orig_name}
%{_pixmapsdir}/%{_orig_name}
