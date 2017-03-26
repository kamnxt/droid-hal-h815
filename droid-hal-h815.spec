# These and other macros are documented in dhd/droid-hal-device.inc
%define device h815
%define vendor lge

%define vendor_pretty LG
%define device_pretty G4 (H815)

%define installable_zip 1

%define droid_target_aarch64 1

%define straggler_files \
/init.baseband.sh\
/init.class_main.sh\
/init.msm8992.sensor.sh\
%{nil}


%include rpm/dhd/droid-hal-device.inc

