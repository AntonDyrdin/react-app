#!/bin/sh
"""true"
# Extended shebang: Detect and run using default Python
python3 -c 1 2>/dev/null && exec python3 "$0" "$@"
python -c 1 2>/dev/null && exec python "$0" "$@"
exit 127
"""
"""
This is the pagekite.py Main() function.
"""
##############################################################################

from __future__ import absolute_import

LICENSE = """\
This file is part of pagekite.py.
Copyright 2010-2026, the Beanstalks Project ehf. and Bjarni Runar Einarsson

This program is free software: you can redistribute it and/or modify it under
the terms of the  GNU  Affero General Public License as published by the Free
Software Foundation, either version 3 of the License, or (at your option) any
later version.

This program is distributed in the hope that it will be useful,  but  WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public License for more
details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see: <http://www.gnu.org/licenses/>
"""
##############################################################################
def main():
  import sys
  from pagekite import pk
  from pagekite import httpd

  if hasattr(sys.stdout, 'isatty') and sys.stdout.isatty():
    import pagekite.ui.basic
    uiclass = pagekite.ui.basic.BasicUi
  else:
    import pagekite.ui.nullui
    uiclass = pagekite.ui.nullui.NullUi

  pk.Main(pk.PageKite, pk.Configure,
          uiclass=uiclass,
          http_handler=httpd.UiRequestHandler,
          http_server=httpd.UiHttpServer)

if __name__ == "__main__":
  main()

##############################################################################
CERTS="""\
ISRG Root X1
============
-----BEGIN CERTIFICATE-----
MIIFazCCA1OgAwIBAgIRAIIQz7DSQONZRGPgu2OCiwAwDQYJKoZIhvcNAQELBQAwTzELMAkGA1UE
BhMCVVMxKTAnBgNVBAoTIEludGVybmV0IFNlY3VyaXR5IFJlc2VhcmNoIEdyb3VwMRUwEwYDVQQD
EwxJU1JHIFJvb3QgWDEwHhcNMTUwNjA0MTEwNDM4WhcNMzUwNjA0MTEwNDM4WjBPMQswCQYDVQQG
EwJVUzEpMCcGA1UEChMgSW50ZXJuZXQgU2VjdXJpdHkgUmVzZWFyY2ggR3JvdXAxFTATBgNVBAMT
DElTUkcgUm9vdCBYMTCCAiIwDQYJKoZIhvcNAQEBBQADggIPADCCAgoCggIBAK3oJHP0FDfzm54r
Vygch77ct984kIxuPOZXoHj3dcKi/vVqbvYATyjb3miGbESTtrFj/RQSa78f0uoxmyF+0TM8ukj1
3Xnfs7j/EvEhmkvBioZxaUpmZmyPfjxwv60pIgbz5MDmgK7iS4+3mX6UA5/TR5d8mUgjU+g4rk8K
b4Mu0UlXjIB0ttov0DiNewNwIRt18jA8+o+u3dpjq+sWT8KOEUt+zwvo/7V3LvSye0rgTBIlDHCN
Aymg4VMk7BPZ7hm/ELNKjD+Jo2FR3qyHB5T0Y3HsLuJvW5iB4YlcNHlsdu87kGJ55tukmi8mxdAQ
4Q7e2RCOFvu396j3x+UCB5iPNgiV5+I3lg02dZ77DnKxHZu8A/lJBdiB3QW0KtZB6awBdpUKD9jf
1b0SHzUvKBds0pjBqAlkd25HN7rOrFleaJ1/ctaJxQZBKT5ZPt0m9STJEadao0xAH0ahmbWnOlFu
hjuefXKnEgV4We0+UXgVCwOPjdAvBbI+e0ocS3MFEvzG6uBQE3xDk3SzynTnjh8BCNAw1FtxNrQH
usEwMFxIt4I7mKZ9YIqioymCzLq9gwQbooMDQaHWBfEbwrbwqHyGO0aoSCqI3Haadr8faqU9GY/r
OPNk3sgrDQoo//fb4hVC1CLQJ13hef4Y53CIrU7m2Ys6xt0nUW7/vGT1M0NPAgMBAAGjQjBAMA4G
A1UdDwEB/wQEAwIBBjAPBgNVHRMBAf8EBTADAQH/MB0GA1UdDgQWBBR5tFnme7bl5AFzgAiIyBpY
9umbbjANBgkqhkiG9w0BAQsFAAOCAgEAVR9YqbyyqFDQDLHYGmkgJykIrGF1XIpu+ILlaS/V9lZL
ubhzEFnTIZd+50xx+7LSYK05qAvqFyFWhfFQDlnrzuBZ6brJFe+GnY+EgPbk6ZGQ3BebYhtF8GaV
0nxvwuo77x/Py9auJ/GpsMiu/X1+mvoiBOv/2X/qkSsisRcOj/KKNFtY2PwByVS5uCbMiogziUwt
hDyC3+6WVwW6LLv3xLfHTjuCvjHIInNzktHCgKQ5ORAzI4JMPJ+GslWYHb4phowim57iaztXOoJw
TdwJx4nLCgdNbOhdjsnvzqvHu7UrTkXWStAmzOVyyghqpZXjFaH3pO3JLF+l+/+sKAIuvtd7u+Nx
e5AW0wdeRlN8NwdCjNPElpzVmbUq4JUagEiuTDkHzsxHpFKVK7q4+63SM1N95R1NbdWhscdCb+ZA
JzVcoyi3B43njTOQ5yOf+1CceWxG1bQVs5ZufpsMljq4Ui0/1lvh+wjChP4kqKOJ2qxq4RgqsahD
YVvTH9w7jXbyLeiNdd8XM2w9U/t7y0Ff/9yi0GE44Za4rF2LN9d11TPAmRGunUHBcnWEvgJBQl9n
JEiU0Zsnvgc/ubhPgXRR4Xq37Z0j4r7g1SgEEzwxA57demyPxgcYxn/eR44/KJ4EBs+lVDR3veyJ
m+kXQ99b21/+jh5Xos1AnX5iItreGCc=
-----END CERTIFICATE-----

ISRG Root X2
============
-----BEGIN CERTIFICATE-----
MIICGzCCAaGgAwIBAgIQQdKd0XLq7qeAwSxs6S+HUjAKBggqhkjOPQQDAzBPMQswCQYDVQQGEwJV
UzEpMCcGA1UEChMgSW50ZXJuZXQgU2VjdXJpdHkgUmVzZWFyY2ggR3JvdXAxFTATBgNVBAMTDElT
UkcgUm9vdCBYMjAeFw0yMDA5MDQwMDAwMDBaFw00MDA5MTcxNjAwMDBaME8xCzAJBgNVBAYTAlVT
MSkwJwYDVQQKEyBJbnRlcm5ldCBTZWN1cml0eSBSZXNlYXJjaCBHcm91cDEVMBMGA1UEAxMMSVNS
RyBSb290IFgyMHYwEAYHKoZIzj0CAQYFK4EEACIDYgAEzZvVn4CDCuwJSvMWSj5cz3es3mcFDR0H
ttwW+1qLFNvicWDEukWVEYmO6gbf9yoWHKS5xcUy4APgHoIYOIvXRdgKam7mAHf7AlF9ItgKbppb
d9/w+kHsOdx1ymgHDB/qo0IwQDAOBgNVHQ8BAf8EBAMCAQYwDwYDVR0TAQH/BAUwAwEB/zAdBgNV
HQ4EFgQUfEKWrt5LSDv6kviejM9ti6lyN5UwCgYIKoZIzj0EAwMDaAAwZQIwe3lORlCEwkSHRhtF
cP9Ymd70/aTSVaYgLXTWNLxBo1BfASdWtL4ndQavEi51mI38AjEAi/V3bNTIZargCyzuFJ0nN6T5
U6VR5CmD1/iQMVtCnwr1/q4AaOeMSQ+2b1tbFfLn
-----END CERTIFICATE-----

Sectigo Public Server Authentication Root E46
=============================================
-----BEGIN CERTIFICATE-----
MIICOjCCAcGgAwIBAgIQQvLM2htpN0RfFf51KBC49DAKBggqhkjOPQQDAzBfMQswCQYDVQQGEwJH
QjEYMBYGA1UEChMPU2VjdGlnbyBMaW1pdGVkMTYwNAYDVQQDEy1TZWN0aWdvIFB1YmxpYyBTZXJ2
ZXIgQXV0aGVudGljYXRpb24gUm9vdCBFNDYwHhcNMjEwMzIyMDAwMDAwWhcNNDYwMzIxMjM1OTU5
WjBfMQswCQYDVQQGEwJHQjEYMBYGA1UEChMPU2VjdGlnbyBMaW1pdGVkMTYwNAYDVQQDEy1TZWN0
aWdvIFB1YmxpYyBTZXJ2ZXIgQXV0aGVudGljYXRpb24gUm9vdCBFNDYwdjAQBgcqhkjOPQIBBgUr
gQQAIgNiAAR2+pmpbiDt+dd34wc7qNs9Xzjoq1WmVk/WSOrsfy2qw7LFeeyZYX8QeccCWvkEN/U0
NSt3zn8gj1KjAIns1aeibVvjS5KToID1AZTc8GgHHs3u/iVStSBDHBv+6xnOQ6OjQjBAMB0GA1Ud
DgQWBBTRItpMWfFLXyY4qp3W7usNw/upYTAOBgNVHQ8BAf8EBAMCAYYwDwYDVR0TAQH/BAUwAwEB
/zAKBggqhkjOPQQDAwNnADBkAjAn7qRaqCG76UeXlImldCBteU/IvZNeWBj7LRoAasm4PdCkT0RH
lAFWovgzJQxC36oCMB3q4S6ILuH5px0CMk7yn2xVdOOurvulGu7t0vzCAxHrRVxgED1cf5kDW21U
SAGKcw==
-----END CERTIFICATE-----

Sectigo Public Server Authentication Root R46
=============================================
-----BEGIN CERTIFICATE-----
MIIFijCCA3KgAwIBAgIQdY39i658BwD6qSWn4cetFDANBgkqhkiG9w0BAQwFADBfMQswCQYDVQQG
EwJHQjEYMBYGA1UEChMPU2VjdGlnbyBMaW1pdGVkMTYwNAYDVQQDEy1TZWN0aWdvIFB1YmxpYyBT
ZXJ2ZXIgQXV0aGVudGljYXRpb24gUm9vdCBSNDYwHhcNMjEwMzIyMDAwMDAwWhcNNDYwMzIxMjM1
OTU5WjBfMQswCQYDVQQGEwJHQjEYMBYGA1UEChMPU2VjdGlnbyBMaW1pdGVkMTYwNAYDVQQDEy1T
ZWN0aWdvIFB1YmxpYyBTZXJ2ZXIgQXV0aGVudGljYXRpb24gUm9vdCBSNDYwggIiMA0GCSqGSIb3
DQEBAQUAA4ICDwAwggIKAoICAQCTvtU2UnXYASOgHEdCSe5jtrch/cSV1UgrJnwUUxDaef0rty2k
1Cz66jLdScK5vQ9IPXtamFSvnl0xdE8H/FAh3aTPaE8bEmNtJZlMKpnzSDBh+oF8HqcIStw+Kxwf
GExxqjWMrfhu6DtK2eWUAtaJhBOqbchPM8xQljeSM9xfiOefVNlI8JhD1mb9nxc4Q8UBUQvX4yMP
FF1bFOdLvt30yNoDN9HWOaEhUTCDsG3XME6WW5HwcCSrv0WBZEMNvSE6Lzzpng3LILVCJ8zab5vu
ZDCQOc2TZYEhMbUjUDM3IuM47fgxMMxF/mL50V0yeUKH32rMVhlATc6qu/m1dkmU8Sf4kaWD5Qaz
Yw6A3OASVYCmO2a0OYctyPDQ0RTp5A1NDvZdV3LFOxxHVp3i1fuBYYzMTYCQNFu31xR13NgESJ/A
wSiItOkcyqex8Va3e0lMWeUgFaiEAin6OJRpmkkGj80feRQXEgyDet4fsZfu+Zd4KKTIRJLpfSYF
plhym3kT2BFfrsU4YjRosoYwjviQYZ4ybPUHNs2iTG7sijbt8uaZFURww3y8nDnAtOFr94MlI1fZ
EoDlSfB1D++N6xybVCi0ITz8fAr/73trdf+LHaAZBav6+CuBQug4urv7qv094PPK306Xlynt8xhW
6aWWrL3DkJiy4Pmi1KZHQ3xtzwIDAQABo0IwQDAdBgNVHQ4EFgQUVnNYZJX5khqwEioEYnmhQBWI
IUkwDgYDVR0PAQH/BAQDAgGGMA8GA1UdEwEB/wQFMAMBAf8wDQYJKoZIhvcNAQEMBQADggIBAC9c
mTz8Bl6MlC5w6tIyMY208FHVvArzZJ8HXtXBc2hkeqK5Duj5XYUtqDdFqij0lgVQYKlJfp/imTYp
E0RHap1VIDzYm/EDMrraQKFz6oOht0SmDpkBm+S8f74TlH7Kph52gDY9hAaLMyZlbcp+nv4fjFg4
exqDsQ+8FxG75gbMY/qB8oFM2gsQa6H61SilzwZAFv97fRheORKkU55+MkIQpiGRqRxOF3yEvJ+M
0ejf5lG5Nkc/kLnHvALcWxxPDkjBJYOcCj+esQMzEhonrPcibCTRAUH4WAP+JWgiH5paPHxsnnVI
84HxZmduTILA7rpXDhjvLpr3Etiga+kFpaHpaPi8TD8SHkXoUsCjvxInebnMMTzD9joiFgOgyY9m
pFuiTdaBJQbpdqQACj7LzTWb4OE4y2BThihCQRxEV+ioratF4yUQvNs+ZUH7G6aXD+u5dHn5Hrwd
Vw1Hr8Mvn4dGp+smWg9WY7ViYG4A++MnESLn/pmPNPW56MORcr3Ywx65LvKRRFHQV80MNNVIIb/b
E/FmJUNS0nAiNs2fxBx1IK1jcmMGDw4nztJqDby1ORrp0XZ60Vzk50lJLVU3aPAaOpg+VBeHVOmm
J1CJeyAvP/+/oYtKR5j/K3tJPsMpRmAYQqszKbrAKbkTidOIijlBO8n9pu0f9GBj39ItVQGL
-----END CERTIFICATE-----

USERTrust RSA Certification Authority
=====================================
-----BEGIN CERTIFICATE-----
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
Q+6IHdfGjjxDah2nGN59PRbxYvnKkKj9
-----END CERTIFICATE-----

USERTrust ECC Certification Authority
=====================================
-----BEGIN CERTIFICATE-----
MIICjzCCAhWgAwIBAgIQXIuZxVqUxdJxVt7NiYDMJjAKBggqhkjOPQQDAzCBiDELMAkGA1UEBhMC
VVMxEzARBgNVBAgTCk5ldyBKZXJzZXkxFDASBgNVBAcTC0plcnNleSBDaXR5MR4wHAYDVQQKExVU
aGUgVVNFUlRSVVNUIE5ldHdvcmsxLjAsBgNVBAMTJVVTRVJUcnVzdCBFQ0MgQ2VydGlmaWNhdGlv
biBBdXRob3JpdHkwHhcNMTAwMjAxMDAwMDAwWhcNMzgwMTE4MjM1OTU5WjCBiDELMAkGA1UEBhMC
VVMxEzARBgNVBAgTCk5ldyBKZXJzZXkxFDASBgNVBAcTC0plcnNleSBDaXR5MR4wHAYDVQQKExVU
aGUgVVNFUlRSVVNUIE5ldHdvcmsxLjAsBgNVBAMTJVVTRVJUcnVzdCBFQ0MgQ2VydGlmaWNhdGlv
biBBdXRob3JpdHkwdjAQBgcqhkjOPQIBBgUrgQQAIgNiAAQarFRaqfloI+d61SRvU8Za2EurxtW2
0eZzca7dnNYMYf3boIkDuAUU7FfO7l0/4iGzzvfUinngo4N+LZfQYcTxmdwlkWOrfzCjtHDix6Ez
nPO/LlxTsV+zfTJ/ijTjeXmjQjBAMB0GA1UdDgQWBBQ64QmG1M8ZwpZ2dEl23OA1xmNjmjAOBgNV
HQ8BAf8EBAMCAQYwDwYDVR0TAQH/BAUwAwEB/zAKBggqhkjOPQQDAwNoADBlAjA2Z6EWCNzklwBB
HU6+4WMBzzuqQhFkoJ2UOQIReVx7Hfpkue4WQrO/isIJxOzksU0CMQDpKmFHjFJKS04YcPbWRNZu
9YO6bVi9JNlWSOrvxKJGgYhqOkbRqZtNyWHa0V1Xahg=
-----END CERTIFICATE-----
"""
PK    2]-\ñ™'Ë  ë     pagekite/android.pyµXYè€Hí~ÁØ </=êßDâ:{◊$oJ<ƒKâﬁ˜!¢®_?Iï›eó€n4vñPâTdD‰ëq±>|¯ÄËq“¢”≈Z8IâÜ}ÈuI™ÊI•ﬂTâèﬁÇ¶ùËUàûú(8&]Ç|Ä*˛Òüº$l™˝¸9Ïªæ	>Fì¢Æöu‹∂ ˚.¯¸˙Aû§%çF?°ƒˇæ&y0YS;P≠!–lZè/Y’cìDqá.±ˆØ%∂‹||ZHNŸvNûµË©©“¿Î– _PßÙQ"uö2A’ætîN‡w€V%Ú∫]›TQ„”éah[Ö›‡4¡ÔËXı®Áîh¯I€5âë£I7©úCøïüÑ„DËK?hê	E4E;Åû~†¨d†(√†©P6(É∆…—SÔÊâá
âîmÄ:¿Di„¿G›Ò)«@àˆ TPΩ3ùÊG4H‡zÛ«)‚_w˙¢Ì#
a˝ÊtÚ≠ÍIËüÓà‰N˜&˜Ú£Âo˙(åüIg\’–ûjÉIû£nÄˆmˆ˘GÖ¨(jÚ:':$5Å™I∑˛ÚvqóÉ[™	vû@≈–ú∆)ªqB-“*…A~@Ø[pÜ◊%Z”FVQÄûÄ™Û§! =ÍI÷Ë’Ç‡©qrÏØ˝>®	?Ëú$o°Õ<Œ"À}4vn<V/HnóÉz0™æ˙Ú/u#N^ï—”L(ÊGàè—≤Í>¢m √Áø„Æ´üœáaxâ ˛•j¢y˛™¢ùˇœˇC÷}I≤vlø>æ•Nˆå¥ÏáÖ	£?≠=˙+D…™ìfÓouVπÈ?GPÙ˘Ù“xœÏÑÈ:o}œi¸˘öº0˙_P:n|n€¸ë'.‰◊õ>xÆæºWé IKEÈS°¯U˛<±œü?L˚¬Eh–K€˘0¶^í÷È∫Ò∑'"}oLüº∏Nõxœ≈>Òrßm·ﬁ?¨ø”∑ë@æ oÉﬂﬂÛg/RüÁp˝±—@∞/_+Ê«7}|äæ^_|˙rˇvirÓÁ÷ç<h>==˝b$jpÌÉ∂„^…?∞∑As˚ÜõÉwÌIÇ˚è∆Õ?íVuÌ”≥k¨∫$,ﬁBÁø üæΩêMA≥ºÑN<√ì@ßüTD‰yÜIIí‡fxDèe◊8Kÿ˝Ä@Q@ëDK—Ç2,öàER3Ü;ıòx•3‘"À^¡‰.EÀ"^Ô"£öyk]î;ì„ïπ“©≥ÑYó¶,˜Oﬂ1õ\›ŸXØÎ≠é–ÜD4≥Ÿ¯Ê9hm_@/jŸp,Í¨(=¨Wúsûëtù$(*tLª∂ñºÔ˚ØÚ»SÅN«"±cIÌ jºãS
} ™•Y¶⁄9Êx∏{•ö∫K¨wÒC)´•ÉÖHâwÈA„‚√√d¶∫ î.>â"ıqà\p'‡
ﬂ“Añã¢≤(Ââîß˚‡·áÿ6°œR æÚy–g∆πvYUk`¿ì˘H›gô—ß•õ´¢œ*Ω®V–°œuÅæ3î¢ÑQ+à¥ˆπ,RŸÛÄ)]ã§˜t<∏ãëZr[#t"ey}6/Sä·˝Ê&ﬂ)∏Û:ø=uÑThì.òÃ5Û^·^OÀÇß%˚—~êD˘x&4ÄL§
"+##ã[Kç )»H◊ÍQ˘JØ;≥hHóøIßEåS∏ﬁä≥˚b'–C√eyÓ“∑keP}( 9≈À≈—6rk^zyõG3§Z{Îv{πÒ„¿o§‰Êç≥ıhù™≠N#gÊ¬CY9^&§tH∫~π5Sgÿûì£1Ê⁄6∞:êÙëZÕã√·cC®%ã	 G&A:QƒØD∞õ|È”MÃÖ·¡Åp7êS¸©ÿ	⁄LÅà+D{Ú!T§ò°xâ'õüâù!•0ºª:ÒS-ŒR•∏ÚN	û;ã<ßE?·GûKtWçhùøJ?‰ÔÊﬂØ“˘ª˘˜´ÙC~ñQDÉØé•≈	·ßÒ¸	9¬©pOhf§¬\cµõèg*±S*≠!o†Î`Ò6,w•D4ÒzäÄIàŒ$Y∞ÏåÊ	ÑRîÑI˛éâ`$¢<ä≥àào1	'}P≠‘·TÒ®Í&,•‹+ï˛Ω©ê¶4∫‰:ıäa8ÇÔí—ö¨c>6¬∏Oë	ÖPæÛ¡∏‰ÔM„	r0è≈õ‡ü…!ˆ∏Ø›BÕr=8ò[b8ÈÙ]‘ˇ§¿è¢ı¥K\¶ö s◊0ÇdúS"≈"ÁßÖ◊Ì 3÷-„ì_’ßmsÚŸQà/õxN\{aû◊˚C8c~ëÕ{ñró
„º‹]E´YËov5Ür-oD*ïn'.-oqmﬂÃ;•πTŸ%ß•-/»r∞⁄«}w–ò¯x6ñF≤›^ÖG!∏)ﬂ#iÁTZÜ—◊HK‘è≠síA”%a‚=gvÙpnín¸æô˛…ıW˝ïuÿ_]ˆ≠ø˛‡WˆWb/*Ì@æˆñù¢a–+œ<&cQBå◊∞°`ÿD:ßf∞‹7"˘Z»ªòÀsÍ_9O´µΩÃ1À|_ˆç»XÊ•[‰=b?æÔﬂ*ˇã^1p±'âî5»:ÏÄzÜ!R*.Õâ¯x#>iÈ_õıﬁ*‰ˇb÷{´êøc,˘â∞oK‘t8 ¨xí¿Ä@Ü#®‡Ò*ëHÌ·∆ﬁŸêK¬¸“/ƒ55zÖ`∫’®¡£œÒ]&´»Œjqî•[¥Z'ß¡-ñ˜ì¥ëjexï/Ó;Jl∞qvõ˜◊A9Áe◊*l®\üøòÅ1	oBY9kfb,fSµtdb_†ºPZX©∂¯zép’ºﬂÍ∫B{Å˘8Û˚>=ô∏Å‰£;jÎ9yHÊõNµ</=„cz˜◊m™÷ëJ€~á1‰e∂uÕ(s	ƒ™„Ü‡"∫Û r£vñ~º&Î˙⁄SöäÁª~ÓØ+≥‡z≤¢õ«öä≥ÕC8u{h|f«≥<5já,O6Ω∫H	˜∏¡ŒNËÁ‰‹Jâ_Ø∑„w˜Æ}{î~??ôŒébúk≥é˘\Ø|„[Üî≠|'w7ô(Ç€ÃF6≥∏’/Ñ{4Mwjˇq‹b0àõ˝Q⁄»W/òŸ˝~Ùä®˘≈rMÆÛÄ◊◊€ï≤fK˘zeÁ,®ﬁ·“ê™-ÊÍlnuπDg…dWßp=ÈûÊÏiæ€ü…≠πJ äõ≈u≤;ö∫Zimë]Â™,nıöœí9“ó]=„(nVV¯Rä$¨¥OÁ˘LÈf≤äu¯m(H‹~¿ØÎ’€Iö‚|Úhù0ﬂ∫´fuçËcjœÓ)€5g1“Ò–≈Ÿˆ™#5»∫†∆ ôÀç‘œGk»Á¶Ä[˘•ªb˚v≥kÓÆø72_$Ω« ’ªπ©∏∫˚§i|€ã>!i⁄¿S@D£ŸÄ#?»Vû≥àN ∆7r@ò˙(ßÏ`Ëã$pV˜:Ø»a—CØÑÌ˝ö)Lü3ÀÇ≈
sËì¢8€QdüIÌsÉÍãL;Gp≠»Ñ=¸§!oùkˇ∞K)µ¥≈‘˛z?¥"ŸGGîqrÆ|N‰dwõË?vΩWY‰;aû'.Ø∞#>ü)hÓé•'Ô∂!"öªê†… Vg†C¥É≈NoáÄà6˘ÂØ˚&‹ypó˜⁄¬≥ﬁc’B§ñ$[v*Á,ıLí?ë#OËSÈ!◊Ôgë|0®º≥Mµ∂.j.îDfß$ÅÅ74∞gë'áªıµû)—4∑πÊy¥ñyÏí†˙¶Œ’_Êπ·Ÿp‘+ëc˜NMòm*ëŒÊ±U‰≠sQ◊à@£m2œ©|Oxÿ¶Ù:‘êµhõ>TLàéπ®!Í'›´»]Zx¶ÅËõR ∏{my
Õ®›Â*R.gÃa˜„¥œ7óÕS8E∆~¡Lo<âÀ6úJ£i:z?!ﬂMG¯W·ı`≥÷œÁ7*˙n~É„[AGæyó˙;≥‹èM»‰Ä)F{œZ¢t∫(ÒyΩ'˚áC”´«l√:1mMèCmw:Ó´ w	¨8ΩÆ Mp/n^^Äló¬	¡uá;b˝÷ëƒµù.£Cé≤M˚Ü”ìæ=?Ú&[E“≈cãy ÛhÒ’¿ôa2itº‰·“j˝à.r#6ã]Ω≈ÆZAÕﬁX-WUåÈTF4Å|Ãv-I6}ëq-©/ß√#Ù3Kö6˚´ˆﬁÉﬁ–M≤kÔ\ÜÑ÷å0ÏjõZ%¶€R<jÎÀg7˚L-*âXî∞kÌ‰+©¨”ïcèá¿S©4≥«’RY“◊9~PW´ƒ&p$l•∆iJjƒT°·%ôÖú@¨⁄–yâ·ÀáR˚ÂÍB$–‡t<”å8‚I€Â≈ÓÃ®ö-È˛Viï,í6BWNŒ~÷(V/lÚ!Ü-è¬«Éö≤≤P‰Î~ôGTaX∞ïè∂Àê®Ì’=l1/,zº¥)åO˚~vÆ»xªí∆ï∫5XwŒf7¢AílLO¨Ñ8≤ú¿ùè›Ïºß˜¡äbaLt¬AXYZJäáAÌIó’≤æƒk=Ge nÖ·ë?‚±mÁ£K£:î50Ê·‘Ü∑aΩæû£æ˜î∏lŒ}Å"›åõ¨Rd?UéssæÂÃ9íC™-è3æ™∏≠¥R)+°éÎÖ-ÿA3sE:ÀF-ñ‰ñôØ´§©ª˝iŒ‰Ür-Dˆ˙ÿÛë|ÁUMÖDã’ØÜ‡ÈöˇPK    2]-\*èı	-  Å£     pagekite/httpd.pyÕ}˝s€6“Ô˛+Pw¸êjeŸN“Œçjπ„ÿJ‚´ø^[π¥èÎ—P$±¶HÜ§¸—N˛˜wwÒÕ……•˜úÁÆÅ≈b±X,ã∞πππ1òá9ÉˇsŒ“`∆Ô¬Çw“'6ZÜQ±∆Ï›`p…rû›Û¨≥±	%6¶Y≤`√·tY,3>≤pë&Y¡ÇQûDÀÇ≈wXöÖq©Ò∏ìxc„€Ø˙∑qzr‘?øÓ≥ZÕõÜ«6¶‘üLÌvv6éíÙ)gÛÇΩÿ›€›~±˚‚«6q„5‚º¢ªú]f…|\0>üvXOÿÎ?Ç,Ÿ’22÷·øyéç°Í“,ôe¡kúfú≥<ôA∆ªÏ)Y≤q≥åO¬º»¬∞ãÖ¢‹I2∂H&·Ù	ñÒÑgHE¡≥EéD„{{˛û±√Èîg	{Àcûª\é¢pÃN√1èsŒ  SÚ9ü∞—ï{dl\K2ÿõ–»˝6„!‰g:7áoˆR’$±µêÂRû±$≈B- ˜i#

SÆSmπi‡ÑÅ!ŒyíB{ÊÄZ¯Fq∂Ã˘tµ\¡ÿáì¡ªã˜Éç√Ûﬂÿá√´´√Û¡o?l1O õﬂsÅ	D)
14'‚‚	©>Î_Ω¯√◊'ß'Éﬂê7'ÉÛ˛ıı∆õã+v».Ø'GÔOØÿÂ˚´ÀãÎ~á±kŒ	#2v5_ß‘Aﬂò"£⁄¸tgîE6Ó9tÎòá˜@W¿∆ UäókqoQœ®ôP¿Ë;ô≤8)⁄0 A|ˆÁEëvwv:≥xŸI≤ŸN$P‰;48øÚhÉ8;ã‰ûÁjÁ…¯éB)î@:GoOPe\S¶* Ø¯«%œãw ÔQµ‰2ã¢p‘ÅQös≠-c¯1o≥èÀ§ y\∆ÍGQfâ»™·8IÓBûó+z\DY:Êâ◊(T¸◊≥”´À#A|€I+—æ!ãçÇúˇ¯j£»û∫˛dÚxn«1OvB)˝,K2$‚≥`¸4H≥X@f¿ÿ‰E∏‡
)Q?/ë*…Ûqê“HøÜòŸP∆:VñULÚ9tÅ˙LrıƒﬁÈz˝ı§A
æHQ—ÍÔy∆ÉIœt6I˝ŒÇ1„;)aZ#èì≈Ùê˚Æöõ¢˙PπZH‹“»N˙UàíŸHB˘≥cØH:9è@·£$
Ä≠Oõ˘xÑT}mll˘∞HÜÿÉ0©éÏËÿ¸Û "	üÇ	ˆÊ¸—††Ö]ñqò1c’Ã˜G"ª’»I8~ZÛ¿3øµÅìËªÑ¸-†˚80Å©ßÄ)/g†‚˘7Ïˆ3∆˝∆8
Úú.ã9âíﬂ'ÈBıè$¶ê)…ü.äa˛…˝1L+ÂÜSFÏÄΩ¯Œﬂ€}ÒÍ;˝üñ≤çﬁ÷‰Ìkèm1QöÌÏ∞2|´a◊Y#Æ4øî0–ÜA îØπ⁄ÌC§)tF≠¢£ZêW√aá≈pËÉ<M€Äî†⁄¿Œbéä@íÉπLRY&> Õ4ÅL?…	Æ3	≥8Xp_#j|ÂO¡£÷r¥Lí,¿/ô,©2uéL∞àÉqáíÅê)djÃD¶XX`v#1òL2û#§Ô-„ª8yàΩ6€µI%”Œ`¢oì˝ ≥ïnÍ8ﬁ {z_8rDøÄ:äs¥hÜ»Ÿ;¯≥’U=è_
x7ei3ØÑ∆·÷f0≤sÜv?ùáF&åbÔ◊Ì+Yp˚ätŸV˛{ˆ{,Ñj¬Ì~h.y&™±´ö[ëú∆n3Ö≤q≤oÌVπ–
)ºÑÕn`∂åQÇ¸
Â`≥‹˘≤∑Ïä(Wû˜°;X¸ÊIjdﬂ≤≥‡f0∞±SÚ†;M`Që”î
∂‰ò1òß)‘äÿM–ï«0ÔS)*FÌÍ/_√◊_Ã√6{]ˆjw∑ÕºE>Éﬂﬁ∞ı¯ƒ√–€≈Sä^¡ãú9=g†yEXDp9áY‰5LpÀîë-éí…¬Ìß–˝ùÙ¿cüê¥Wª{i$xqI6
'6}àÿ*›D€·xåò«`nwÿuíeOﬂ8ÙΩ,”˜Ú+—˜ÚÎ–˜™Lﬂ+ãæÛ§ ªVC_@ﬂ+fïn¢’ÆD@?É˝êdOhÕãB5‘˛∞ªÎR	µ'(”1¨§@}&…àΩå¢âÓÎœ—RÇ’»"Ã«I<g∞éü`kFYr«„jÆ.^_Æø‹VºpZqÒK-ÂiñîWù∂Uæ˜ÊömPFq—eﬂÅ“´ü·®ÃqòÉzH∫lg5‡∑éœ4\∞å¿⁄MFIëwä«J∑†iÄ·Ï‰¨?¸vŸø∆∆JÔÂ,E˙Ô√	Ov‡#ÖñŸÿÉ`å˘¡r&;¯!öÁE≤†åñ±cZâÔ`⁄˜èÿ{ê~º¯!ÀçT_∏ öw£Ì∂fÙÁã2⁄«Ì—üa˙Baó˘]‚«8Mk{ƒÁπŒ¿ﬂ*‰bJo<ù’„õì
©ãhì€îüåÀ˘ã¸!…‘XÛf·‘?Jºò˝Ye≈X° œ◊pbﬁƒ	b•·V*ài5„—õ|¨4)oè¬l˙Wª
Ïè‡>X≈“?Ç¨åãlŸx