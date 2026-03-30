import React, { useState, useEffect } from 'react';
import { ChevronRight, BookOpen, RotateCw, Plus, Trash2, Eye, EyeOff, TrendingUp, Zap, Volume2, CheckCircle2, AlertCircle } from 'lucide-react';

const GermanLearner = () => {
  const [tab, setTab] = useState('flashcards');
  const [showAnswer, setShowAnswer] = useState(false);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [knownCards, setKnownCards] = useState(new Set());
  const [learningCards, setLearningCards] = useState(new Set());
  const [newWords, setNewWords] = useState('');
  const [newTranslation, setNewTranslation] = useState('');
  const [customCards, setCustomCards] = useState([]);
  const [searchFilter, setSearchFilter] = useState('');
  const [dailyTextIndex, setDailyTextIndex] = useState(0);
  const [notesText, setNotesText] = useState('');

  // Cargar datos guardados
  useEffect(() => {
    const saved = localStorage.getItem('germanData');
    if (saved) {
      const data = JSON.parse(saved);
      setKnownCards(new Set(data.known || []));
      setLearningCards(new Set(data.learning || []));
      setCustomCards(data.custom || []);
      setNotesText(data.notes || '');
    }
  }, []);

  // Guardar datos
  useEffect(() => {
    localStorage.setItem('germanData', JSON.stringify({
      known: Array.from(knownCards),
      learning: Array.from(learningCards),
      custom: customCards,
      notes: notesText
    }));
  }, [knownCards, learningCards, customCards, notesText]);

  // Vocabulario B1 + A1/A2 - ESPAÑOL A ALEMÁN
  const allVocab = [
    // VERBOS IMPORTANTES (Sein/Haben/Werden regulares e irregulares)
    { spanish: 'ser/estar', german: 'sein', category: 'Verbo', level: 'A1' },
    { spanish: 'tener', german: 'haben', category: 'Verbo', level: 'A1' },
    { spanish: 'llegar a ser', german: 'werden', category: 'Verbo', level: 'A1' },
    { spanish: 'ir', german: 'gehen', category: 'Verbo', level: 'A1' },
    { spanish: 'venir', german: 'kommen', category: 'Verbo', level: 'A1' },
    { spanish: 'hacer', german: 'machen', category: 'Verbo', level: 'A1' },
    { spanish: 'ver', german: 'sehen', category: 'Verbo', level: 'A1' },
    { spanish: 'saber', german: 'wissen', category: 'Verbo', level: 'A1' },
    { spanish: 'pensar', german: 'denken', category: 'Verbo', level: 'A2' },
    { spanish: 'sentir', german: 'fühlen', category: 'Verbo', level: 'A2' },
    { spanish: 'dar', german: 'geben', category: 'Verbo', level: 'A1' },
    { spanish: 'hablar', german: 'sprechen', category: 'Verbo', level: 'A1' },
    { spanish: 'decir', german: 'sagen', category: 'Verbo', level: 'A1' },
    { spanish: 'tomar/coger', german: 'nehmen', category: 'Verbo', level: 'A1' },
    { spanish: 'dejar', german: 'lassen', category: 'Verbo', level: 'A1' },
    { spanish: 'encontrar', german: 'finden', category: 'Verbo', level: 'A1' },
    { spanish: 'llevar', german: 'tragen', category: 'Verbo', level: 'A1' },
    { spanish: 'llevar (llevar a alguien)', german: 'bringen', category: 'Verbo', level: 'A1' },
    { spanish: 'conocer', german: 'kennen', category: 'Verbo', level: 'A1' },
    { spanish: 'mostrar', german: 'zeigen', category: 'Verbo', level: 'A1' },
    
    // VERBOS MODALES
    { spanish: 'poder', german: 'können', category: 'Verbo Modal', level: 'A1' },
    { spanish: 'deber', german: 'müssen', category: 'Verbo Modal', level: 'A1' },
    { spanish: 'querer', german: 'wollen', category: 'Verbo Modal', level: 'A1' },
    { spanish: 'deber (obligación)', german: 'sollen', category: 'Verbo Modal', level: 'A1' },
    { spanish: 'estar permitido', german: 'dürfen', category: 'Verbo Modal', level: 'A1' },
    { spanish: 'gustar', german: 'mögen', category: 'Verbo Modal', level: 'A1' },
    { spanish: 'quisiera', german: 'möchte', category: 'Verbo Modal', level: 'A1' },

    // VERBOS B1 IMPORTANTES
    { spanish: 'presentarse', german: 'sich vorstellen', category: 'Verbo', level: 'B1' },
    { spanish: 'discutir', german: 'besprechen', category: 'Verbo', level: 'B1' },
    { spanish: 'pedir', german: 'bitten', category: 'Verbo', level: 'B1' },
    { spanish: 'decidir', german: 'entscheiden', category: 'Verbo', level: 'B1' },
    { spanish: 'permitir', german: 'erlauben', category: 'Verbo', level: 'B1' },
    { spanish: 'aparecer', german: 'erscheinen', category: 'Verbo', level: 'B1' },
    { spanish: 'seguir', german: 'folgen', category: 'Verbo', level: 'B1' },
    { spanish: 'valer (ser válido)', german: 'gelten', category: 'Verbo', level: 'B1' },
    { spanish: 'disfrutar', german: 'genießen', category: 'Verbo', level: 'B1' },
    { spanish: 'creer', german: 'glauben', category: 'Verbo', level: 'A2' },
    { spanish: 'suceder', german: 'geschehen', category: 'Verbo', level: 'B1' },
    { spanish: 'actuar', german: 'handeln', category: 'Verbo', level: 'B1' },
    { spanish: 'colgar', german: 'hängen', category: 'Verbo', level: 'A2' },
    { spanish: 'gobernar', german: 'herrschen', category: 'Verbo', level: 'B1' },
    { spanish: 'esperar', german: 'hoffen', category: 'Verbo', level: 'A2' },
    { spanish: 'traer', german: 'holen', category: 'Verbo', level: 'A2' },
    { spanish: 'oír', german: 'hören', category: 'Verbo', level: 'A1' },
    { spanish: 'amar', german: 'lieben', category: 'Verbo', level: 'A2' },
    { spanish: 'entregar', german: 'liefern', category: 'Verbo', level: 'B1' },
    { spanish: 'estar tendido', german: 'liegen', category: 'Verbo', level: 'A1' },
    { spanish: 'valer la pena', german: 'lohnen', category: 'Verbo', level: 'B1' },
    { spanish: 'resolver', german: 'lösen', category: 'Verbo', level: 'B1' },
    { spanish: 'gestionar', german: 'managen', category: 'Verbo', level: 'B1' },
    { spanish: 'significar', german: 'meinen', category: 'Verbo', level: 'A2' },
    { spanish: 'notar', german: 'merken', category: 'Verbo', level: 'A2' },
    { spanish: 'mezclar', german: 'mischen', category: 'Verbo', level: 'B1' },
    { spanish: 'acercarse', german: 'nähern', category: 'Verbo', level: 'B1' },
    { spanish: 'nombrar', german: 'nennen', category: 'Verbo', level: 'A2' },
    { spanish: 'abrir', german: 'öffnen', category: 'Verbo', level: 'A1' },
    { spanish: 'empacar', german: 'packen', category: 'Verbo', level: 'A2' },
    { spanish: 'encajar', german: 'passen', category: 'Verbo', level: 'A2' },
    { spanish: 'cuidar', german: 'pflegen', category: 'Verbo', level: 'B1' },
    { spanish: 'recoger (flores)', german: 'pflücken', category: 'Verbo', level: 'B1' },
    { spanish: 'charlar', german: 'plaudern', category: 'Verbo', level: 'B1' },
    { spanish: 'elogiar', german: 'preisen', category: 'Verbo', level: 'B1' },
    { spanish: 'probar', german: 'prüfen', category: 'Verbo', level: 'B1' },
    { spanish: 'aconsejar', german: 'raten', category: 'Verbo', level: 'A2' },
    { spanish: 'robar', german: 'rauben', category: 'Verbo', level: 'B1' },
    { spanish: 'hablar (charlar)', german: 'reden', category: 'Verbo', level: 'A2' },
    { spanish: 'alcanzar', german: 'reichen', category: 'Verbo', level: 'A2' },
    { spanish: 'viajar', german: 'reisen', category: 'Verbo', level: 'A1' },
    { spanish: 'rasgar', german: 'reißen', category: 'Verbo', level: 'A2' },
    { spanish: 'correr', german: 'rennen', category: 'Verbo', level: 'A2' },
    { spanish: 'rescatar', german: 'retten', category: 'Verbo', level: 'A2' },

    // SUSTANTIVOS COMUNES A1-A2
    { spanish: 'casa', german: 'Haus', category: 'Sustantivo', level: 'A1' },
    { spanish: 'ciudad', german: 'Stadt', category: 'Sustantivo', level: 'A1' },
    { spanish: 'coche', german: 'Auto', category: 'Sustantivo', level: 'A1' },
    { spanish: 'escuela', german: 'Schule', category: 'Sustantivo', level: 'A1' },
    { spanish: 'trabajo', german: 'Arbeit', category: 'Sustantivo', level: 'A1' },
    { spanish: 'mujer', german: 'Frau', category: 'Sustantivo', level: 'A1' },
    { spanish: 'hombre', german: 'Mann', category: 'Sustantivo', level: 'A1' },
    { spanish: 'niño', german: 'Kind', category: 'Sustantivo', level: 'A1' },
    { spanish: 'agua', german: 'Wasser', category: 'Sustantivo', level: 'A1' },
    { spanish: 'pan', german: 'Brot', category: 'Sustantivo', level: 'A1' },
    { spanish: 'leche', german: 'Milch', category: 'Sustantivo', level: 'A1' },
    { spanish: 'queso', german: 'Käse', category: 'Sustantivo', level: 'A1' },
    { spanish: 'carne', german: 'Fleisch', category: 'Sustantivo', level: 'A1' },
    { spanish: 'pez', german: 'Fisch', category: 'Sustantivo', level: 'A1' },
    { spanish: 'fruta', german: 'Obst', category: 'Sustantivo', level: 'A1' },
    { spanish: 'verdura', german: 'Gemüse', category: 'Sustantivo', level: 'A1' },
    { spanish: 'manzana', german: 'Apfel', category: 'Sustantivo', level: 'A1' },
    { spanish: 'pera', german: 'Birne', category: 'Sustantivo', level: 'A1' },
    { spanish: 'uva', german: 'Traube', category: 'Sustantivo', level: 'A1' },
    { spanish: 'naranja', german: 'Orange', category: 'Sustantivo', level: 'A1' },
    { spanish: 'plátano', german: 'Banane', category: 'Sustantivo', level: 'A1' },
    { spanish: 'mesa', german: 'Tisch', category: 'Sustantivo', level: 'A1' },
    { spanish: 'silla', german: 'Stuhl', category: 'Sustantivo', level: 'A1' },
    { spanish: 'puerta', german: 'Tür', category: 'Sustantivo', level: 'A1' },
    { spanish: 'ventana', german: 'Fenster', category: 'Sustantivo', level: 'A1' },
    { spanish: 'cama', german: 'Bett', category: 'Sustantivo', level: 'A1' },
    { spanish: 'libro', german: 'Buch', category: 'Sustantivo', level: 'A1' },
    { spanish: 'periódico', german: 'Zeitung', category: 'Sustantivo', level: 'A1' },
    { spanish: 'dinero', german: 'Geld', category: 'Sustantivo', level: 'A1' },
    { spanish: 'tiempo', german: 'Zeit', category: 'Sustantivo', level: 'A1' },

    // SUSTANTIVOS B1
    { spanish: 'aventura', german: 'Abenteuer', category: 'Sustantivo', level: 'B1' },
    { spanish: 'superstición', german: 'Aberglaube', category: 'Sustantivo', level: 'B1' },
    { spanish: 'despedida', german: 'Abschied', category: 'Sustantivo', level: 'B1' },
    { spanish: 'sección', german: 'Abschnitt', category: 'Sustantivo', level: 'B1' },
    { spanish: 'intención', german: 'Absicht', category: 'Sustantivo', level: 'B1' },
    { spanish: 'descenso', german: 'Abstieg', category: 'Sustantivo', level: 'B1' },
    { spanish: 'departamento', german: 'Abteilung', category: 'Sustantivo', level: 'B1' },
    { spanish: 'atención', german: 'Achtung', category: 'Sustantivo', level: 'B1' },
    { spanish: 'vena', german: 'Ader', category: 'Sustantivo', level: 'B1' },
    { spanish: 'asunto', german: 'Affäre', category: 'Sustantivo', level: 'B1' },
    { spanish: 'emoción', german: 'Affekt', category: 'Sustantivo', level: 'B1' },
    { spanish: 'mono', german: 'Affe', category: 'Sustantivo', level: 'A2' },
    { spanish: 'pobreza', german: 'Armut', category: 'Sustantivo', level: 'B1' },
    { spanish: 'miedo', german: 'Angst', category: 'Sustantivo', level: 'A2' },
    { spanish: 'comienzo', german: 'Anfang', category: 'Sustantivo', level: 'A1' },
    { spanish: 'oferta', german: 'Angebot', category: 'Sustantivo', level: 'B1' },
    { spanish: 'ataque', german: 'Angriff', category: 'Sustantivo', level: 'B1' },
    { spanish: 'sugerencia', german: 'Anregung', category: 'Sustantivo', level: 'B1' },
    { spanish: 'apariencia', german: 'Anschein', category: 'Sustantivo', level: 'B1' },
    { spanish: 'vista', german: 'Ansicht', category: 'Sustantivo', level: 'B1' },
    { spanish: 'respuesta', german: 'Antwort', category: 'Sustantivo', level: 'A1' },
    { spanish: 'uso', german: 'Anwendung', category: 'Sustantivo', level: 'B1' },
    { spanish: 'signo', german: 'Anzeichen', category: 'Sustantivo', level: 'B1' },
    { spanish: 'anuncio', german: 'Anzeige', category: 'Sustantivo', level: 'B1' },
    { spanish: 'cuenta', german: 'Anzug', category: 'Sustantivo', level: 'A2' },
    { spanish: 'farmacia', german: 'Apotheke', category: 'Sustantivo', level: 'A2' },
    { spanish: 'aparato', german: 'Apparat', category: 'Sustantivo', level: 'B1' },
    { spanish: 'apetito', german: 'Appetit', category: 'Sustantivo', level: 'A2' },
    { spanish: 'aplauso', german: 'Applaus', category: 'Sustantivo', level: 'B1' },

    // ADJETIVOS A1-A2
    { spanish: 'grande', german: 'groß', category: 'Adjetivo', level: 'A1' },
    { spanish: 'pequeño', german: 'klein', category: 'Adjetivo', level: 'A1' },
    { spanish: 'bueno', german: 'gut', category: 'Adjetivo', level: 'A1' },
    { spanish: 'malo', german: 'schlecht', category: 'Adjetivo', level: 'A1' },
    { spanish: 'hermoso', german: 'schön', category: 'Adjetivo', level: 'A1' },
    { spanish: 'feo', german: 'hässlich', category: 'Adjetivo', level: 'A1' },
    { spanish: 'rápido', german: 'schnell', category: 'Adjetivo', level: 'A1' },
    { spanish: 'lento', german: 'langsam', category: 'Adjetivo', level: 'A1' },
    { spanish: 'viejo', german: 'alt', category: 'Adjetivo', level: 'A1' },
    { spanish: 'joven', german: 'jung', category: 'Adjetivo', level: 'A1' },
    { spanish: 'caliente', german: 'heiß', category: 'Adjetivo', level: 'A1' },
    { spanish: 'frío', german: 'kalt', category: 'Adjetivo', level: 'A1' },
    { spanish: 'nuevo', german: 'neu', category: 'Adjetivo', level: 'A1' },
    { spanish: 'largo', german: 'lang', category: 'Adjetivo', level: 'A1' },
    { spanish: 'corto', german: 'kurz', category: 'Adjetivo', level: 'A1' },
    { spanish: 'blanco', german: 'weiß', category: 'Adjetivo', level: 'A1' },
    { spanish: 'negro', german: 'schwarz', category: 'Adjetivo', level: 'A1' },
    { spanish: 'rojo', german: 'rot', category: 'Adjetivo', level: 'A1' },
    { spanish: 'azul', german: 'blau', category: 'Adjetivo', level: 'A1' },
    { spanish: 'verde', german: 'grün', category: 'Adjetivo', level: 'A1' },

    // ADJETIVOS B1
    { spanish: 'gastado', german: 'abgenutzt', category: 'Adjetivo', level: 'B1' },
    { spanish: 'dependiente', german: 'abhängig', category: 'Adjetivo', level: 'B1' },
    { spanish: 'abominable', german: 'abscheulich', category: 'Adjetivo', level: 'B1' },
    { spanish: 'extraño', german: 'absonderlich', category: 'Adjetivo', level: 'B1' },
    { spanish: 'anticuado', german: 'abständig', category: 'Adjetivo', level: 'B1' },
    { spanish: 'ausente', german: 'abwesend', category: 'Adjetivo', level: 'B1' },
    { spanish: 'atento', german: 'achtsam', category: 'Adjetivo', level: 'B1' },
    { spanish: 'afectado', german: 'affig', category: 'Adjetivo', level: 'B1' },
    { spanish: 'agresivo', german: 'aggressiv', category: 'Adjetivo', level: 'B1' },
    { spanish: 'tonto', german: 'albern', category: 'Adjetivo', level: 'B1' },
    { spanish: 'solo', german: 'allein', category: 'Adjetivo', level: 'A1' },
    { spanish: 'general', german: 'allgemein', category: 'Adjetivo', level: 'B1' },
    { spanish: 'cotidiano', german: 'alltäglich', category: 'Adjetivo', level: 'B1' },
    { spanish: 'demasiado', german: 'allzu', category: 'Adjetivo', level: 'B1' },
    { spanish: 'familiar', german: 'altbekannt', category: 'Adjetivo', level: 'B1' },
    { spanish: 'venerable', german: 'altehrwürdig', category: 'Adjetivo', level: 'B1' },
  ];

  const filteredVocab = [...allVocab, ...customCards].filter(card => {
    const matchesSearch = card.spanish.toLowerCase().includes(searchFilter.toLowerCase()) ||
                         card.german.toLowerCase().includes(searchFilter.toLowerCase());
    return matchesSearch;
  });

  const currentCard = filteredVocab[currentIndex] || filteredVocab[0];
  const progress = {
    total: filteredVocab.length,
    known: knownCards.size,
    learning: learningCards.size,
    new: filteredVocab.length - knownCards.size - learningCards.size
  };

  const markAsKnown = () => {
    if (currentCard) {
      setKnownCards(new Set([...knownCards, currentCard.spanish]));
      setLearningCards(prev => new Set([...prev].filter(w => w !== currentCard.spanish)));
      moveNext();
    }
  };

  const markAsLearning = () => {
    if (currentCard) {
      setLearningCards(new Set([...learningCards, currentCard.spanish]));
      setKnownCards(prev => new Set([...prev].filter(w => w !== currentCard.spanish)));
      moveNext();
    }
  };

  const markAsNew = () => {
    if (currentCard) {
      setKnownCards(prev => new Set([...prev].filter(w => w !== currentCard.spanish)));
      setLearningCards(prev => new Set([...prev].filter(w => w !== currentCard.spanish)));
      moveNext();
    }
  };

  const moveNext = () => {
    if (currentIndex < filteredVocab.length - 1) {
      setCurrentIndex(currentIndex + 1);
    } else {
      setCurrentIndex(0);
    }
    setShowAnswer(false);
  };

  const addCustomCard = () => {
    if (newWords.trim() && newTranslation.trim()) {
      const newCard = {
        spanish: newWords.trim(),
        german: newTranslation.trim(),
        category: 'Custom',
        level: 'B1'
      };
      setCustomCards([...customCards, newCard]);
      setNewWords('');
      setNewTranslation('');
    }
  };

  const deleteCard = (spanish) => {
    setCustomCards(customCards.filter(c => c.spanish !== spanish));
  };

  const textosDiarios = [
    {
      titulo: 'Ein Tag im Leben (A1)',
      texto: 'Ich heiße Anna und ich bin 28 Jahre alt. Ich wohne in Berlin mit meiner Familie. Jeden Morgen stehe ich um 7 Uhr auf. Ich nehme eine Dusche und esse Frühstück. Um 8 Uhr gehe ich zur Arbeit. Ich arbeite in einem Büro. Meine Arbeit ist interessant. Ich habe viele Kollegen und wir arbeiten gut zusammen. Um 12 Uhr machen wir Mittagspause. Ich esse mit meinen Freunden zu Mittag. Um 17 Uhr fahre ich nach Hause. Zu Hause mache ich die Hausaufgaben und koche Dinner. Am Abend lese ich ein Buch oder sehe fern. Um 22 Uhr gehe ich ins Bett.',
      vocabulario: ['Frühstück (breakfast)', 'Büro (office)', 'Kollege (colleague)', 'Mittagspause (lunch break)', 'Hausaufgaben (homework)', 'ins Bett gehen (go to bed)']
    },
    {
      titulo: 'Beim Einkaufen (A2)',
      texto: 'Maria geht zum Supermarkt einkaufen. Sie braucht Lebensmittel für das Wochenende. Sie hat eine Einkaufsliste geschrieben. Sie nimmt einen Einkaufskorb und geht in den Laden. Sie kauft Brot, Butter, Käse, Milch und Gemüse. Sie sucht auch Fleisch für das Abendessen. Der Preis ist etwas teuer diesen Monat. An der Kasse steht eine lange Schlange. Sie zahlt mit ihrer Kreditkarte. Die Kassiererin gibt ihr den Kassenzettel und die Tüten. Maria geht nach Hause und packt alles in den Kühlschrank.',
      vocabulario: ['Einkaufen (shopping)', 'Einkaufsliste (shopping list)', 'Supermarkt (supermarket)', 'Lebensmittel (food)', 'Kasse (checkout)', 'Kassiererin (cashier)', 'Tüte (bag)']
    },
    {
      titulo: 'Urlaub planen (A2)',
      texto: 'Die Familie möchte einen Urlaub machen. Sie planen eine Reise nach Italien. Sie mögen das warme Wetter und die schöne Landschaft. Sie buchen ein Hotel in Rom für zwei Wochen. Sie kaufen Flugtickets online. Sie machen auch eine Reisekasse. Sie brauchen einen Reisepass und Reisechecks. Sie packen ihre Koffer schon zwei Wochen vorher. Sie sind sehr aufgeregt und können kaum warten. Die Reise wird sicher wunderbar!',
      vocabulario: ['Urlaub (vacation)', 'Reise (trip)', 'buchen (book)', 'Flugticket (flight ticket)', 'Reisepass (passport)', 'Koffer (suitcase)', 'aufgeregt (excited)']
    },
    {
      titulo: 'Schule und Ausbildung (B1)',
      texto: 'Die Schulbildung ist in Deutschland sehr wichtig. Die Grundschule dauert vier Jahre. Danach können Schüler ein Gymnasium, eine Realschule oder eine Hauptschule besuchen. Das Gymnasium dauert neun Jahre und endet mit dem Abitur. Das Abitur ist notwendig, um an einer Universität zu studieren. Die meisten Universitäten in Deutschland sind kostenlos. Nach dem Studium können Absolventen verschiedene Karrieren wählen. Viele junge Menschen machen auch eine Berufsausbildung. Diese Ausbildung ist theoretisch und praktisch. Nach der Ausbildung können sie sofort arbeiten.',
      vocabulario: ['Schulbildung (school education)', 'Grundschule (primary school)', 'Gymnasium (high school)', 'Abitur (final school exam)', 'Universität (university)', 'Berufsausbildung (vocational training)', 'Absolvent (graduate)']
    },
    {
      titulo: 'Umwelt und Klima (B1)',
      texto: 'Der Klimawandel ist eines der größten Probleme unserer Zeit. Die Temperaturen steigen immer mehr. Das Eis in der Arktis schmilzt schneller. Die Meere werden wärmer und der Meeresspiegel steigt. Viele Tier- und Pflanzenarten sind gefährdet. Die Menschheit muss etwas dagegen tun. Wir müssen Energie sparen und weniger Autos fahren. Wir sollten mehr öffentliche Verkehrsmittel benutzen. Recycling und Umweltschutz sind wichtig. Viele Länder investieren in erneuerbare Energien wie Windkraft und Solarenergie. Jeder Mensch kann seinen Beitrag leisten.',
      vocabulario: ['Klimawandel (climate change)', 'Temperatur (temperature)', 'Eis (ice)', 'Meeresspiegel (sea level)', 'Meeresspiegel (sea level)', 'Energie (energy)', 'Recycling (recycling)', 'erneuerbare Energien (renewable energy)', 'Windkraft (wind power)']
    },
    {
      titulo: 'Technologie und Innovation (B1)',
      texto: 'Die Technologie entwickelt sich sehr schnell. Das Internet hat die Welt verändert. Smartphones sind überall und fast jeder benutzt sie täglich. Künstliche Intelligenz wird immer wichtiger. Roboter können jetzt viele menschliche Aufgaben übernehmen. Die Cloud ermöglicht es uns, überall auf unsere Daten zuzugreifen. Viele Menschen arbeiten im Home Office. Die Sicherheit im Internet ist aber auch ein großes Problem. Wir müssen unsere persönlichen Daten schützen. Die Technologie hilft auch bei der Lösung von vielen Problemen wie Krankheiten und Hunger.',
      vocabulario: ['Technologie (technology)', 'Internet (internet)', 'Smartphone (smartphone)', 'Künstliche Intelligenz (artificial intelligence)', 'Roboter (robot)', 'Cloud (cloud)', 'Sicherheit (security)', 'persönliche Daten (personal data)']
    }
  ];

  const currentText = textosDiarios[dailyTextIndex];

  const speak = (text) => {
    if ('speechSynthesis' in window) {
      const utterance = new SpeechSynthesisUtterance(text);
      utterance.lang = 'de-DE';
      window.speechSynthesis.cancel();
      window.speechSynthesis.speak(utterance);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-950 via-blue-950 to-slate-900" style={{fontFamily: "'Poppins', sans-serif"}}>
      {/* Header Premium */}
      <div className="bg-gradient-to-r from-blue-700 via-indigo-700 to-purple-700 text-white p-8 shadow-2xl border-b-4 border-purple-500">
        <div className="max-w-7xl mx-auto">
          <div className="flex items-center gap-3 mb-3">
            <BookOpen size={40} className="animate-pulse" />
            <h1 className="text-5xl font-black tracking-tight">DEUTSCH MEISTER</h1>
          </div>
          <p className="text-blue-100 text-lg font-light">Aprendizaje inteligente de alemán • B1 + A1/A2 • Sistema de repetición espaciada</p>
        </div>
      </div>

      {/* Navigation */}
      <div className="bg-slate-800/80 backdrop-blur-md border-b border-slate-700 sticky top-0 z-50">
        <div className="max-w-7xl mx-auto flex flex-wrap gap-2 p-4">
          {[
            { id: 'flashcards', label: '🎴 Flashcards', icon: '✨' },
            { id: 'textos', label: '📖 Textos Diarios', icon: '📚' },
            { id: 'stats', label: '📊 Estadísticas', icon: '📈' },
            { id: 'add', label: '➕ Añadir Palabras', icon: '📝' }
          ].map(t => (
            <button
              key={t.id}
              onClick={() => setTab(t.id)}
              className={`px-6 py-3 rounded-xl font-bold transition-all duration-300 transform ${
                tab === t.id
                  ? 'bg-gradient-to-r from-purple-600 to-indigo-600 text-white shadow-lg scale-105'
                  : 'bg-slate-700 text-slate-300 hover:bg-slate-600'
              }`}
            >
              {t.icon} {t.label}
            </button>
          ))}
        </div>
      </div>

      <div className="max-w-7xl mx-auto p-8">
        {/* FLASHCARDS */}
        {tab === 'flashcards' && (
          <div className="grid grid-cols-1 lg:grid-cols-4 gap-8">
            {/* Card Principal */}
            <div className="lg:col-span-3">
              <div className="h-96 bg-gradient-to-br from-purple-600 via-indigo-600 to-blue-600 rounded-3xl p-12 shadow-2xl text-white flex flex-col justify-center items-center cursor-pointer transform transition-all duration-300 hover:scale-105 hover:shadow-3xl" onClick={() => setShowAnswer(!showAnswer)}>
                {!showAnswer ? (
                  <div className="text-center">
                    <p className="text-blue-100 text-lg mb-6 font-light">Palabra en ESPAÑOL</p>
                    <h2 className="text-6xl font-black mb-8 tracking-wider">{currentCard?.spanish}</h2>
                    <p className="text-blue-200 flex items-center justify-center gap-2">
                      <Eye size={20} /> Click para ver la traducción
                    </p>
                  </div>
                ) : (
                  <div className="text-center">
                    <p className="text-indigo-200 text-lg mb-6 font-light">Traducción en ALEMÁN</p>
                    <h2 className="text-5xl font-black mb-6">{currentCard?.german}</h2>
                    <div className="flex gap-4 justify-center">
                      <button
                        onClick={(e) => {
                          e.stopPropagation();
                          speak(currentCard?.german);
                        }}
                        className="px-6 py-3 bg-blue-500 hover:bg-blue-600 rounded-xl font-bold transition-all flex items-center gap-2"
                      >
                        <Volume2 size={20} /> Pronunciar
                      </button>
                      <p className="text-indigo-200 flex items-center gap-2">
                        <EyeOff size={20} /> Click para ocultar
                      </p>
                    </div>
                  </div>
                )}
              </div>

              {/* Card Info */}
              <div className="grid grid-cols-3 gap-4 mt-8">
                <div className="bg-slate-700 rounded-2xl p-6 text-white text-center">
                  <p className="text-slate-300 text-sm mb-2">Categoría</p>
                  <p className="text-2xl font-bold text-blue-400">{currentCard?.category}</p>
                </div>
                <div className="bg-slate-700 rounded-2xl p-6 text-white text-center">
                  <p className="text-slate-300 text-sm mb-2">Nivel</p>
                  <p className="text-2xl font-bold text-purple-400">{currentCard?.level}</p>
                </div>
                <div className="bg-slate-700 rounded-2xl p-6 text-white text-center">
                  <p className="text-slate-300 text-sm mb-2">Progreso</p>
                  <p className="text-2xl font-bold text-green-400">{currentIndex + 1}/{filteredVocab.length}</p>
                </div>
              </div>

              {/* Buttons */}
              <div className="flex gap-4 mt-8 flex-wrap">
                <button
                  onClick={markAsNew}
                  className="flex-1 px-6 py-4 bg-slate-600 hover:bg-slate-700 text-white rounded-xl font-bold transition-all duration-300 flex items-center justify-center gap-2"
                >
                  <AlertCircle size={20} /> Aún No Sé
                </button>
                <button
                  onClick={markAsLearning}
                  className="flex-1 px-6 py-4 bg-yellow-600 hover:bg-yellow-700 text-white rounded-xl font-bold transition-all duration-300 flex items-center justify-center gap-2"
                >
                  <Zap size={20} /> Aprendiendo
                </button>
                <button
                  onClick={markAsKnown}
                  className="flex-1 px-6 py-4 bg-green-600 hover:bg-green-700 text-white rounded-xl font-bold transition-all duration-300 flex items-center justify-center gap-2"
                >
                  <CheckCircle2 size={20} /> Lo Sé
                </button>
              </div>

              {/* Search & Filter */}
              <div className="mt-8">
                <input
                  type="text"
                  placeholder="Buscar palabra en español o alemán..."
                  value={searchFilter}
                  onChange={(e) => {
                    setSearchFilter(e.target.value);
                    setCurrentIndex(0);
                  }}
                  className="w-full px-6 py-4 bg-slate-700 text-white rounded-xl border-2 border-slate-600 focus:border-purple-500 outline-none transition-all placeholder-slate-400"
                />
              </div>
            </div>

            {/* Sidebar Stats */}
            <div className="lg:col-span-1 space-y-6">
              <div className="bg-gradient-to-br from-green-600 to-emerald-600 rounded-2xl p-6 text-white">
                <p className="text-green-100 text-sm mb-2">Dominio Total</p>
                <p className="text-4xl font-black">{progress.known}</p>
                <p className="text-green-200 text-sm mt-2">palabras memorizadas</p>
              </div>

              <div className="bg-gradient-to-br from-yellow-600 to-orange-600 rounded-2xl p-6 text-white">
                <p className="text-yellow-100 text-sm mb-2">En Proceso</p>
                <p className="text-4xl font-black">{progress.learning}</p>
                <p className="text-yellow-200 text-sm mt-2">palabras aprendiendo</p>
              </div>

              <div className="bg-gradient-to-br from-blue-600 to-cyan-600 rounded-2xl p-6 text-white">
                <p className="text-blue-100 text-sm mb-2">Por Aprender</p>
                <p className="text-4xl font-black">{progress.new}</p>
                <p className="text-blue-200 text-sm mt-2">palabras nuevas</p>
              </div>

              <div className="bg-slate-700 rounded-2xl p-6 text-white">
                <p className="text-slate-300 text-sm mb-3 font-bold">Progreso Total</p>
                <div className="w-full bg-slate-600 rounded-full h-4 overflow-hidden">
                  <div
                    className="h-full bg-gradient-to-r from-green-500 via-yellow-500 to-red-500 transition-all duration-500"
                    style={{ width: `${(progress.known / progress.total) * 100}%` }}
                  />
                </div>
                <p className="text-slate-300 text-xs mt-3">{Math.round((progress.known / progress.total) * 100)}% completado</p>
              </div>
            </div>
          </div>
        )}

        {/* TEXTOS DIARIOS */}
        {tab === 'textos' && (
          <div className="space-y-8">
            {/* Selector de textos */}
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
              {textosDiarios.map((texto, idx) => (
                <button
                  key={idx}
                  onClick={() => setDailyTextIndex(idx)}
                  className={`p-6 rounded-2xl transition-all transform ${
                    dailyTextIndex === idx
                      ? 'bg-gradient-to-br from-purple-600 to-indigo-600 text-white scale-105 shadow-xl'
                      : 'bg-slate-700 text-slate-300 hover:bg-slate-600'
                  }`}
                >
                  <h3 className="font-bold text-lg">{texto.titulo}</h3>
                </button>
              ))}
            </div>

            {/* Texto Principal */}
            <div className="bg-gradient-to-br from-slate-700 to-slate-800 rounded-3xl p-12 text-white shadow-2xl">
              <h2 className="text-4xl font-black mb-8 text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-pink-400">{currentText?.titulo}</h2>
              
              <div className="mb-8">
                <p className="text-lg leading-relaxed text-slate-100 font-light mb-6">
                  {currentText?.texto}
                </p>
                <button
                  onClick={() => speak(currentText?.texto)}
                  className="px-6 py-3 bg-blue-600 hover:bg-blue-700 rounded-xl font-bold transition-all flex items-center gap-2"
                >
                  <Volume2 size={20} /> Escuchar pronunciación
                </button>
              </div>

              {/* Vocabulario Clave */}
              <div>
                <h3 className="text-2xl font-bold mb-6 text-purple-300">Vocabulario Clave</h3>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  {currentText?.vocabulario.map((vocab, idx) => (
                    <div key={idx} className="bg-slate-600/50 rounded-xl p-4 border-l-4 border-purple-500">
                      <p className="text-slate-200">{vocab}</p>
                    </div>
                  ))}
                </div>
              </div>
            </div>

            {/* Notas */}
            <div className="bg-slate-700 rounded-2xl p-8 text-white">
              <h3 className="text-2xl font-bold mb-6">Tus Notas</h3>
              <textarea
                value={notesText}
                onChange={(e) => setNotesText(e.target.value)}
                placeholder="Escribe tus notas sobre los textos..."
                className="w-full h-32 bg-slate-600 text-white p-4 rounded-xl border-2 border-slate-500 focus:border-purple-500 outline-none placeholder-slate-400 resize-none"
              />
            </div>
          </div>
        )}

        {/* ESTADÍSTICAS */}
        {tab === 'stats' && (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            <div className="bg-gradient-to-br from-blue-600 to-cyan-600 rounded-2xl p-8 text-white text-center">
              <p className="text-blue-100 text-sm mb-3 font-light">Total de Palabras</p>
              <p className="text-5xl font-black">{progress.total}</p>
              <p className="text-blue-200 text-sm mt-3">en el sistema</p>
            </div>

            <div className="bg-gradient-to-br from-green-600 to-emerald-600 rounded-2xl p-8 text-white text-center">
              <p className="text-green-100 text-sm mb-3 font-light">Palabras Dominadas</p>
              <p className="text-5xl font-black">{progress.known}</p>
              <p className="text-green-200 text-sm mt-3">{Math.round((progress.known / progress.total) * 100)}% completado</p>
            </div>

            <div className="bg-gradient-to-br from-yellow-600 to-orange-600 rounded-2xl p-8 text-white text-center">
              <p className="text-yellow-100 text-sm mb-3 font-light">En Aprendizaje</p>
              <p className="text-5xl font-black">{progress.learning}</p>
              <p className="text-yellow-200 text-sm mt-3">necesitan repaso</p>
            </div>

            <div className="bg-gradient-to-br from-purple-600 to-pink-600 rounded-2xl p-8 text-white text-center">
              <p className="text-purple-100 text-sm mb-3 font-light">Por Aprender</p>
              <p className="text-5xl font-black">{progress.new}</p>
              <p className="text-purple-200 text-sm mt-3">palabras nuevas</p>
            </div>
          </div>
        )}

        {/* AÑADIR PALABRAS */}
        {tab === 'add' && (
          <div className="max-w-2xl mx-auto space-y-8">
            {/* Formulario */}
            <div className="bg-gradient-to-br from-slate-700 to-slate-800 rounded-3xl p-12 text-white">
              <h2 className="text-3xl font-black mb-8">Añadir Palabras Personalizadas</h2>
              
              <div className="space-y-6">
                <div>
                  <label className="block text-sm font-bold text-slate-300 mb-3">Palabra en ESPAÑOL</label>
                  <input
                    type="text"
                    value={newWords}
                    onChange={(e) => setNewWords(e.target.value)}
                    placeholder="ej: sociedad"
                    className="w-full px-6 py-4 bg-slate-600 text-white rounded-xl border-2 border-slate-500 focus:border-purple-500 outline-none placeholder-slate-400"
                  />
                </div>

                <div>
                  <label className="block text-sm font-bold text-slate-300 mb-3">Traducción en ALEMÁN</label>
                  <input
                    type="text"
                    value={newTranslation}
                    onChange={(e) => setNewTranslation(e.target.value)}
                    placeholder="ej: Gesellschaft"
                    className="w-full px-6 py-4 bg-slate-600 text-white rounded-xl border-2 border-slate-500 focus:border-purple-500 outline-none placeholder-slate-400"
                  />
                </div>

                <button
                  onClick={addCustomCard}
                  className="w-full px-6 py-4 bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-700 hover:to-indigo-700 text-white rounded-xl font-bold transition-all duration-300 flex items-center justify-center gap-2 text-lg"
                >
                  <Plus size={24} /> Agregar Palabra
                </button>
              </div>
            </div>

            {/* Palabras Personalizadas */}
            {customCards.length > 0 && (
              <div className="bg-slate-700 rounded-2xl p-8 text-white">
                <h3 className="text-2xl font-bold mb-6">Tus Palabras Personalizadas ({customCards.length})</h3>
                <div className="space-y-3">
                  {customCards.map((card, idx) => (
                    <div key={idx} className="bg-slate-600 p-4 rounded-xl flex justify-between items-center">
                      <div>
                        <p className="font-bold text-lg">{card.spanish}</p>
                        <p className="text-slate-300">{card.german}</p>
                      </div>
                      <button
                        onClick={() => deleteCard(card.spanish)}
                        className="px-4 py-2 bg-red-600 hover:bg-red-700 rounded-lg transition-all"
                      >
                        <Trash2 size={18} />
                      </button>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
        )}
      </div>

      {/* Footer */}
      <div className="bg-slate-900 border-t border-slate-700 mt-16 py-8 text-center text-slate-400">
        <p className="text-sm">DEUTSCH MEISTER © 2024 | Sistema inteligente de aprendizaje de alemán</p>
      </div>
    </div>
  );
};

export default GermanLearner;
