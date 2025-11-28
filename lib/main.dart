import 'package:flutter/material.dart';
import 'screens/home_screen.dart';

void main() {
  runApp(const SmartTradingApp());
}

class SmartTradingApp extends StatelessWidget {
  const SmartTradingApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'SmartTrading D366',
      home: HomeScreen(),
    );
  }
}
