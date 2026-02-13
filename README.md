# DHCP Starvation Attack – Scapy

## Descripción

El ataque DHCP Starvation tiene como objetivo agotar el pool de direcciones IP disponibles en un servidor DHCP mediante el envío masivo de solicitudes DHCP Discover utilizando direcciones MAC falsificadas. Cuando el pool se consume completamente, los clientes legítimos no pueden obtener configuración de red, generando una denegación de servicio (DoS).

---

## Objetivo del Script

Desarrollar un script en Scapy capaz de generar múltiples solicitudes DHCP Discover con direcciones MAC aleatorias para consumir todas las direcciones IP disponibles en el servidor DHCP.

---

## Topología de Red

**Componentes:**

* Router configurado como servidor DHCP
* Switch de acceso
* Host atacante (Kali Linux)
* Host víctima

**Direccionamiento IP:**

| Dispositivo | Dirección               |
| ----------- | ----------------------- |
| Router      | 10.9.23.1               |
| Pool DHCP   | 10.9.23.2 – 10.9.23.254 |
| Atacante    | DHCP                    |
| Víctima     | DHCP                    |

**VLAN:** VLAN 1 (por defecto)

**Interfaces relevantes:**

* Kali Linux → Ethernet0/1
* Switch → Ethernet0/0 (uplink hacia el router)



## Parámetros Utilizados

| Parámetro  | Descripción                                         |
| ---------- | --------------------------------------------------- |
| iface      | Interfaz de red utilizada para el envío de paquetes |
| random_mac | Generación de direcciones MAC aleatorias            |
| loop       | Envío continuo de solicitudes DHCP                  |

---

## Requisitos

* Sistema operativo Linux (preferiblemente Kali Linux)
* Python 3
* Scapy
* Permisos de superusuario
* Conectividad de Capa 2 con el servidor DHCP
* Entorno de virtualización (PNETLab, EVE-NG o GNS3)

**Instalación de Scapy:**
pip install scapy


## Impacto del Ataque

* Denegación de servicio a clientes legítimos.
* Interrupción de la conectividad de red.
* Degradación del rendimiento.
* Posible preparación para ataques posteriores como DHCP Rogue.

**Nivel de severidad: Alto**

---

## Medidas de Mitigación

### DHCP Snooping

Permite filtrar mensajes DHCP provenientes de puertos no confiables.

ip dhcp snooping
ip dhcp snooping vlan 1


### Port Security

Limita la cantidad de direcciones MAC permitidas por puerto.

switchport port-security
switchport port-security maximum 5


### Rate Limiting

Restringe la cantidad de solicitudes DHCP que un puerto puede generar.


## Conclusión

El laboratorio demostró que un atacante puede agotar rápidamente el pool DHCP mediante solicitudes falsificadas, afectando la disponibilidad de la red y comprometiendo la operación de los dispositivos legítimos.
