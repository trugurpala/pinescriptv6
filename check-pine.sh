#!/bin/bash
# Pine Script v6 versiyon kontrolü
# Kullanım: ./check-pine.sh
echo "=== Pine Script v6 Version Check ==="
FAIL=0
for f in $(find examples global-markets webhook-templates -name "*.pine" 2>/dev/null); do
  if ! head -3 "$f" | grep -q "//@version=6"; then
    echo "❌ //@version=6 eksik: $f"
    FAIL=1
  else
    echo "✅ $f"
  fi
done
if [ $FAIL -eq 0 ]; then
  echo ""
  echo "✅ Tüm .pine dosyaları //@version=6 içeriyor"
fi
exit $FAIL
