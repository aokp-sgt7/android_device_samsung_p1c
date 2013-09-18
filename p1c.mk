DEVICE_PACKAGE_OVERLAYS := device/samsung/p1c/overlay

$(call inherit-product, device/samsung/p1-common/device_base.mk)
$(call inherit-product-if-exists, vendor/samsung/p1c/p1c-vendor.mk)

$(call inherit-product, $(SRC_TARGET_DIR)/product/full.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/languages_full.mk)

# Init files
PRODUCT_COPY_FILES += \
    device/samsung/p1c/fstab.p1c:root/fstab.p1c \
    device/samsung/p1c/init.p1c.rc:root/init.p1c.rc \
    device/samsung/p1c/ueventd.p1c.rc:root/ueventd.p1c.rc \
    device/samsung/p1c/init.recovery.rc:root/init.recovery.p1c.rc \
    device/samsung/p1c/init.p1c.usb.rc:root/init.p1c.usb.rc \
    device/samsung/p1c/init.p1c.usb.rc:recovery/root/usb.rc

# vold
PRODUCT_COPY_FILES += \
    device/samsung/p1c/prebuilt/etc/vold.fstab:system/etc/vold.fstab

# RIL
PRODUCT_COPY_FILES += \
    device/samsung/p1c/prebuilt/etc/ppp/ip-up:system/etc/ppp/ip-up \
    frameworks/native/data/etc/android.hardware.telephony.cdma.xml:system/etc/permissions/android.hardware.telephony.cdma.xml

# Verizon cdma stuff
PRODUCT_PROPERTY_OVERRIDES += \
       ro.telephony.default_network=4 \
       ro.ril.def.agps.mode=2 \
       ro.ril.samsung_cdma=true \
       ro.cdma.home.operator.numeric=310004 \
       ro.cdma.home.operator.alpha=VzW \
       ro.cdma.homesystem=64,65,76,77,78,79,80,81,82,83 \
       ro.cdma.data_retry_config=default_randomization=2000,0,0,120000,180000,540000,960000 \
       ro.cdma.otaspnumschema=SELC,3,00,07,80,87,88,99 \
       net.cdma.pppd.authtype=require-chap \
       net.cdma.pppd.user=user[SPACE]VerizonWireless \
       net.cdma.datalinkinterface=/dev/ttyCDMA0 \
       net.cdma.ppp.interface=ppp0 \
       net.connectivity.type=CDMA1 \
       net.interfaces.defaultroute=cdma \
       rild.libpath=/system/lib/libsec-ril40.so \
       rild.libargs=-d/dev/ttyS0 \
       mobiledata.interfaces=wlan0,ppp0

#Set build fingerprint / ID / Product Name ect.
PRODUCT_BUILD_PROP_OVERRIDES += PRODUCT_NAME=SCH-I800 TARGET_DEVICE=SCH-I800 BUILD_FINGERPRINT=verizon/SCH-I800/SCH-I800:2.3.4/GINGERBREAD/EF01:user/release-keys PRIVATE_BUILD_DESC="SCH-I800-user 2.3.4 GINGERBREAD EF01 release-keys"

