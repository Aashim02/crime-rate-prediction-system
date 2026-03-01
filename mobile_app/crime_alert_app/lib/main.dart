import 'package:flutter/material.dart';
import 'alert_screen.dart';

void main() {
  runApp(const CrimeAlertApp());
}

class CrimeAlertApp extends StatelessWidget {
  const CrimeAlertApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Crime Alert App',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.indigo),
      ),
      home: const AlertScreen(),
    );
  }
}
