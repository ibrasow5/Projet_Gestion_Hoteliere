import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_application/client_hotel.dart';
import 'package:flutter_application/dalayed_animation.dart';
import 'package:flutter_application/facture.dart';
import 'package:flutter_application/liste_chambre.dart';
import 'package:flutter_application/reservation_hotel.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:flutter_application/main.dart';
import 'package:flutter_application/info_hotel.dart';
import 'package:flutter_application/statistique_hotel.dart';

class MenuPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        elevation: 0,
        backgroundColor:d_red,
        leading: IconButton(
          icon: Icon(
            Icons.arrow_back,
            color: Colors.black,
            size: 30,
          ),
          onPressed: () {
            Navigator.pop(context);
          },
        ),
        title: Text(
          'MENU PRINCIPAL',
          style: TextStyle(
            fontWeight: FontWeight.bold,
            fontSize: 22,
          ),
        ),
      ),
      body: SingleChildScrollView(
        child: Column(
          children: [
            Container(
              margin: EdgeInsets.symmetric(
                vertical: 5,
                horizontal: 5,
              ),
              child: Column(
                children: [
                  SizedBox(height: 5),
                  Container(
                    width: 800,
                    height: 300,
                    decoration: BoxDecoration(
                      border: Border.all(
                        width: 2,
                        color: d_red,
                      )
                    ),
                    child: Image.asset(
                      'assets/image/Menu.png',
                      fit: BoxFit.cover,
                      ),
                    ),
                  SizedBox(height: 20),
                  ElevatedButton(
                    onPressed: () {
                      Navigator.push(
                        context,
                        MaterialPageRoute(builder: (context) => InfoHotel(),
                        ),
                      );
                    },
                    style: ElevatedButton.styleFrom(
                      backgroundColor: d_red,
                      shape: StadiumBorder(),
                      padding: EdgeInsets.all(13),
                    ),
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        Icon(Icons.hotel),
                        SizedBox(width: 10),
                        Text('GESTION D\'HOTEL'),
                      ],
                    ),
                  ),
                  SizedBox(height: 20),
                  ElevatedButton(
                    onPressed: () {
                      Navigator.push(
                        context,
                        MaterialPageRoute(builder: (context) => Listechambre(),
                        ),
                      );
                    },
                    style: ElevatedButton.styleFrom(
                      backgroundColor: d_red,
                      shape: StadiumBorder(),
                      padding: EdgeInsets.all(13),
                    ),
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        Icon(Icons.hotel),
                        SizedBox(width: 10),
                        Text('LES CHAMBRES'),
                      ],
                    ),
                  ),
                  SizedBox(height: 20),
                  ElevatedButton(
                    onPressed: () {
                      Navigator.push(
                        context,
                        MaterialPageRoute(builder: (context) => ClientHotel(),
                        ),
                      );
                      },
                    style: ElevatedButton.styleFrom(
                      backgroundColor: d_red,
                      shape: StadiumBorder(),
                      padding: EdgeInsets.all(13),
                    ),
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        Icon(Icons.person),
                        SizedBox(width: 10),
                        Text('LES CLIENTS'),
                      ],
                    ),
                  ),
                  SizedBox(height: 20),

                  ElevatedButton(
                    onPressed: () {
                      Navigator.push(
                        context,
                        MaterialPageRoute(builder: (context) => ReservationHotel(),
                        ),
                      );
                      },
                    style: ElevatedButton.styleFrom(
                      backgroundColor: d_red,
                      shape: StadiumBorder(),
                      padding: EdgeInsets.all(13),
                    ),
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        Icon(Icons.calendar_today),
                        SizedBox(width: 10),
                        Text('LES RÉSERVATIONS'),
                      ],
                    ),
                  ),
                  SizedBox(height: 20),
                  ElevatedButton(
                    onPressed: () {
                      Navigator.push(
                        context,
                        MaterialPageRoute(builder: (context) => Facture(),
                        ),
                      );
                      },
                    style: ElevatedButton.styleFrom(
                      backgroundColor: d_red,
                      shape: StadiumBorder(),
                      padding: EdgeInsets.all(13),
                    ),
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        Icon(Icons.receipt),
                        SizedBox(width: 10),
                        Text('LES FACTURES'),
                      ],
                    ),
                  ),
                  SizedBox(height: 40),
                  ElevatedButton(
                    onPressed: () {
                      Navigator.pop(context);
                    },
                    style: ElevatedButton.styleFrom(
                      backgroundColor: d_red,
                      shape: StadiumBorder(),
                      padding: EdgeInsets.all(13),
                    ),
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        Icon(Icons.exit_to_app),
                        SizedBox(width: 10),
                        Text('QUITTER'),
                      ],
                    ),
                  ),
                  SizedBox(height: 20),
                ],
              ),
            )
          ],
        ),
      ),
    );
  }
}