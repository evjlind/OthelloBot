#include<string>
#include <vector>
#include <shared_mutex>
#include <cstdint>
#include <deque>
#include <unordered_map>
#include <unistd.h>
#include <cmath>
#include<SDL2/include/SDL2/SDL.h>

#include "../../../cc-lib/threadutil.h"
#include "../../../cc-lib/randutil.h"
#include "../../../cc-lib/arcfour.h"

#include "../othello.h"

#define CHECKMARK "\xF2"
#define ESC "\xF3"
#define HEART "\xF4"
/* here L means "long" */
#define LCMARK1 "\xF5"
#define LCMARK2 "\xF6"
#define LCHECKMARK LCMARK1 LCMARK2
#define LRARROW1 "\xF7"
#define LRARROW2 "\xF8"
#define LRARROW LRARROW1 LRARROW2
#define LLARROW1 "\xF9"
#define LLARROW2 "\xFA"
#define LLARROW LLARROW1 LLARROW2

/* BAR_0 ... BAR_10 are guaranteed to be consecutive */
#define BAR_0 "\xE0"
#define BAR_1 "\xE1"
#define BAR_2 "\xE2"
#define BAR_3 "\xE3"
#define BAR_4 "\xE4"
#define BAR_5 "\xE5"
#define BAR_6 "\xE6"
#define BAR_7 "\xE7"
#define BAR_8 "\xE8"
#define BAR_9 "\xE9"
#define BAR_10 "\xEA"
#define BARSTART "\xEB"

#define FONTCHARS " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789`-=[]\\;',./~!@#$%^&*()_+{}|:\"<>?" CHECKMARK ESC HEART LCMARK1 LCMARK2 BAR_0 BAR_1 BAR_2 BAR_3 BAR_4 BAR_5 BAR_6 BAR_7 BAR_8 BAR_9 BAR_10 BARSTART LRARROW LLARROW

#define FONTSTYLES 7

using namespace std;

using int64 = int64_t;
using uint32 = uint32_t;