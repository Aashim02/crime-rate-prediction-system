import 'package:flutter/material.dart';

class AlertScreen extends StatelessWidget {
  const AlertScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Crime Alerts')),
      body: const Center(
        child: Text(
          'No high-risk alerts currently.',
          style: TextStyle(fontSize: 18),
        ),
      ),
    );
  }
}
