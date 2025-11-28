import 'package:flutter/material.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("SmartTrading D366"),
        centerTitle: true,
      ),
      body: const Center(
        child: Text(
          "Welcome — App Loaded Successfully!",
          style: TextStyle(fontSize: 20),
        ),
      ),
    );
  }
}
