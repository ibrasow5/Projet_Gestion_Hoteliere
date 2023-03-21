import 'package:flutter/material.dart';
import 'package:flutter_application/welcome_page.dart';

const d_red = Color.fromARGB(255, 24, 144, 144);

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Bienvenue dans notre hôtel',
      debugShowCheckedModeBanner: false,
      home: WelcomePage(),
    );
  }
}
