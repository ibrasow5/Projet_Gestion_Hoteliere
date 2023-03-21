import 'package:flutter/material.dart';
import 'package:flutter_application/dalayed_animation.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:flutter_application/main.dart';
import 'package:flutter_application/menu_page.dart';

class WelcomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor:Color(0xFFEDECF2),
       appBar: AppBar(
        backgroundColor: d_red,
        title: Text('Welcome'),
      ),
      body: SingleChildScrollView(
        child: Container(
          margin: EdgeInsets.symmetric(
            vertical: 5,
            horizontal: 05,
          ),
          child: Column(
            children: [
              DelayedAnimation(
                delay: 1500,
                child: Container(
                  width: 200,
                  height: 200,
                  decoration: BoxDecoration(
                      border: Border.all(
                        width: 2,
                        color: d_red,
                      )
                    ),
                  child: Image.asset(
                    'assets/image/logo.png',
                    fit: BoxFit.fill,
                  ),
                ), 
              ), 
              SizedBox(height: 0),
              DelayedAnimation(
                delay: 1500,
                child: Container(
                  width: 800,
                  height: 350,
                  decoration: BoxDecoration(
                      border: Border.all(
                        width: 2,
                        color: d_red,
                      )
                    ),
                  child: Image.asset(
                    'assets/image/me.png',
                    fit: BoxFit.fill,
                  ),
                ), 
              ), 
              SizedBox(height: 0),
              DelayedAnimation(
                delay: 2500,
                child: Container(
                  margin: EdgeInsets.only(top: 30, bottom: 20),
                  child: Text(
                    'Bienvenue dans l\'hotel TERANGA',
                    textAlign: TextAlign.center,
                    style: TextStyle(
                      fontSize: 30,
                    ),
                  ),
                ), 
              ), 
              SizedBox(height: 10),
              DelayedAnimation(
                delay: 4500,
                child: Container(
                  width: double.infinity,
                  child: ElevatedButton(
                    style: ElevatedButton.styleFrom(
                      backgroundColor: d_red,
                      shape: StadiumBorder(),
                      padding: EdgeInsets.all(13)
                    ),
                    child: Text('DEMARRER'),
                    onPressed: () {
                      Navigator.push(
                        context,
                        MaterialPageRoute(builder: (context) => MenuPage(),
                        ),
                      );
                    },
                  ),
                ), 
              ),
            ], 
          ), 
        ),
      ),
    );
  }
}
