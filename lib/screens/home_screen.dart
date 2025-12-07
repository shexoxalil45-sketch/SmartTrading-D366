import 'package:flutter/material.dart';
import '../services/trading_service.dart';
import 'trade_screen.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});
  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  late final TradingService engine;

  @override
  void initState() {
    super.initState();
    engine = TradingService();
    engine.init();
    engine.addListener(() {
      setState(() {});
    });
  }

  @override
  void dispose() {
    engine.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('SmartTrading-D366'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            Text('Bot: ${engine.isRunning ? "Running" : "Stopped"}'),
            const SizedBox(height: 12),
            ElevatedButton(
              onPressed: engine.toggle,
              child: Text(engine.isRunning ? 'Stop Bot' : 'Start Bot'),
            ),
            const SizedBox(height: 16),
            ElevatedButton(
              onPressed: () => Navigator.push(context, MaterialPageRoute(builder: (_) => const TradeScreen())),
              child: const Text('Open Trade Screen'),
            ),
            const SizedBox(height: 20),
            const Text('Logs:'),
            Expanded(
              child: ListView.builder(
                itemCount: engine.logs.length,
                itemBuilder: (c, i) => ListTile(title: Text(engine.logs[i])),
              ),
            )
          ],
        ),
      ),
    );
  }
}
